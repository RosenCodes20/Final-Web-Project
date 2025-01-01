from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from football_team_manager.schedules.forms import CreateEventForm
from football_team_manager.schedules.models import Event, EventAttendance

from football_team_manager.teams.models import MyTeam

UserModel = get_user_model()

# class ScheduleDetails(DetailView):
#
#     model = Event
#     template_name = 'schedule/schedule_details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['my_team'] = self.request.user.myteam_set.first()
#
#         context['events'] = Event.objects.filter(
#             user=self.request.user
#         ).order_by('date')

@login_required
def schedule_details(request, pk):
    user = UserModel.objects.get(id=pk)

    if not request.user == user or not MyTeam.objects.filter(user=user):
        raise PermissionDenied()


    my_team = user.myteam_set.first()

    filtered_events = Event.objects.filter(
        user=user
    ).order_by("date", "time")

    for event in filtered_events:
        date = event.date
        date = datetime.combine(date, datetime.min.time())

        if date < datetime.now():
            event.delete()

    context = {
        "user": user,
        "my_team": my_team,
        "events": filtered_events
    }


    return render(request, 'schedule/schedule_details.html', context)


@login_required
def add_event(request):

    if not MyTeam.objects.filter(user=request.user):
        raise PermissionDenied()

    form = CreateEventForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            event = form.save(commit=False)

            event.user = request.user

            event.save()

            EventAttendance.objects.create(user=request.user, event=event, attended=False)

            return redirect('schedule-details', pk=request.user.pk)

    context = {
        "form": form
    }

    return render(request, 'schedule/add_event.html', context)


@login_required
def all_events(request, pk):
    user = UserModel.objects.get(id=pk)

    if not request.user == user or not MyTeam.objects.filter(user=user):
        raise PermissionDenied()

    my_team = request.user.myteam_set.first()

    events = Event.objects.filter(user=request.user).all().order_by("date", "time")

    context = {
        "events": events,
        'my_team': my_team
    }
    return render(request, 'schedule/schedule_details.html', context)



@login_required
def game_events(request, pk):
    user = UserModel.objects.get(id=pk)

    if not request.user == user or not MyTeam.objects.filter(user=user):
        raise PermissionDenied()

    my_team = request.user.myteam_set.first()

    events = Event.objects.filter(is_training=False, user=request.user).order_by("date", "time")

    context = {
        "events": events,
        'my_team': my_team
    }

    return render(request, 'schedule/schedule_details.html', context)


@login_required
def training_events(request, pk):
    user = UserModel.objects.get(id=pk)

    if not request.user == user or not MyTeam.objects.filter(user=user):
        raise PermissionDenied()

    my_team = request.user.myteam_set.first()

    events = Event.objects.filter(is_training=True, user=request.user).order_by("date", "time")

    context = {
        "events": events,
        'my_team': my_team
    }

    return render(request, 'schedule/schedule_details.html', context)


def event_analytics(request, pk):
    user = UserModel.objects.get(id=pk)

    if not request.user == user:
        raise PermissionDenied()

    total_events = Event.objects.filter(user=request.user).count()

    total_attendance = EventAttendance.objects.filter(user=request.user, attended=True).count()

    attendance_rate = (total_attendance / total_events) * 100 if total_events > 0 else 0

    event_attendance = EventAttendance.objects.filter(user=request.user).values('event__team_versus', 'event__is_training').annotate(
        total=Count('id'),
        attended=Count('id', filter=Q(attended=True))
    )

    context = {
        "total_events": total_events,
        "total_attendance": total_attendance,
        "attendance_rate": attendance_rate,
        "event_attendance": event_attendance
    }

    return render(request, "schedule/event_analytics.html", context)


def attend_functionality(request, pk):

    event = EventAttendance.objects.get(id=pk)

    event.attended = True

    event.save()

    return redirect(request.META["HTTP_REFERER"], user=request.user)


def attend_functionality_to_false(request, pk):
    event = EventAttendance.objects.get(id=pk)

    event.attended = False

    event.save()

    return redirect(request.META["HTTP_REFERER"], user=request.user)