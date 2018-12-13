from datetime import datetime, timedelta
from typing import List, Dict, Tuple


class Event:
    def __init__(self, time: datetime, action: str):
        self.time = time
        self.action = action
        self.is_new = 'Guard' in action

    def __str__(self):
        return "{0} {1}".format(self.time, self.action)


class Session:
    def __init__(self, initial_event: Event):
        self._raw_events = [initial_event]
        self.guardNo = int(initial_event.action.split(' ', 2)[1][1:])
        self.startDate = self._round_date(initial_event.time)
        self.minutes_asleep = 0

    def append(self, event: Event):
        self._raw_events.append(event)

    def asleep_wake_time_pairs(self):
        for i in range(1, len(self._raw_events), 2):
            time_asleep = self._raw_events[i].time
            time_wakes = self._raw_events[i + 1].time
            yield time_asleep, time_wakes

    def process(self):
        for time_asleep, time_wakes in self.asleep_wake_time_pairs():
            self.minutes_asleep += (time_wakes - time_asleep).seconds//60

    def was_asleep(self, minute: int) -> int:
        for time_asleep, time_wakes in self.asleep_wake_time_pairs():
            if time_asleep.minute <= minute < time_wakes.minute:
                return True
        return False

    def _round_date(self, d: datetime):
        return d.replace(minute=0, second=0, hour=d.hour) + timedelta(hours=d.minute//30)


def get_input():
    ''' Break condition used to paste sub-problem into same file.  '''
    with open('4_input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            yield line


def load_ordered() -> List[Event]:
    events = []
    for line in get_input():
        date_str = line[:18]
        event = line[19:]
        date = datetime.strptime(date_str, '[%Y-%m-%d %H:%M]')
        events.append(Event(date, event))
    return sorted(events, key=lambda e: e.time)


def load_sessions() -> List[Session]:
    current_session = None
    sessions = []
    for event in load_ordered():
        if event.is_new:
            current_session = Session(event)
            sessions.append(current_session)
        else:
            current_session.append(event)

    for s in sessions:
        s.process()
    return sessions


def load_sessions_per_guard() -> Dict[int, List[Session]]:
    sessions_per_guard = {}
    for session in load_sessions():
        if session.guardNo not in sessions_per_guard:
            sessions_per_guard[session.guardNo] = []
        sessions_per_guard[session.guardNo].append(session)
    return sessions_per_guard


def get_most_often_aslsep_tuple(sessions: List[Session]) -> Tuple[int, int]:
    times_asleep_per_minute = [0]*60
    for minute in range(60):
        times_asleep_per_minute[minute] = sum(s.was_asleep(minute) for s in sessions)
    most_times_asleep = max(times_asleep_per_minute)
    most_times_asleep_minute = times_asleep_per_minute.index(most_times_asleep)
    return most_times_asleep, most_times_asleep_minute


def get_most_sleepy_guard(sessions_per_guard: Dict[int, List[Session]]) -> int:
    asleep_per_guard = {guard: sum(s.minutes_asleep
                                   for s in sessions) for guard, sessions in sessions_per_guard.items()}
    most_asleep_guard_no = max(asleep_per_guard, key=asleep_per_guard.get)
    return most_asleep_guard_no


def part_one() -> int:
    sessions_per_guard = load_sessions_per_guard()
    sleepy_guard_no = get_most_sleepy_guard(sessions_per_guard)
    most_sleepy_minute = get_most_often_aslsep_tuple(sessions_per_guard[sleepy_guard_no])[1]
    return sleepy_guard_no * most_sleepy_minute


def part_two() -> int:
    sessions_per_guard = load_sessions_per_guard()
    most_often_asleep_per_guard = []
    for guard, sessions in sessions_per_guard.items():
        times, minute = get_most_often_aslsep_tuple(sessions)
        most_often_asleep_per_guard.append((guard, times, minute))
    most_often_asleep_guard = max(most_often_asleep_per_guard, key=lambda tupl: tupl[1])
    guard, times, minute = most_often_asleep_guard
    return guard * minute


print(part_one())
print(part_two())

