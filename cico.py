import os
import rumps
from datetime import datetime
from datetime import timedelta


def current_timestamp():
    timestamp_string = f'{datetime.now().date()} at {datetime.now().time().strftime("%H:%M")}'
    return timestamp_string


current_timestamp()


class CiCo(rumps.App):

    @rumps.clicked("👨‍💻️ Check in")
    def check_in(self, _):
        with open('timestamps.txt', 'a') as timestamps:
            global last_login
            last_login = datetime.now().time()
            timestamps.writelines(f'\nchecked in:  {current_timestamp()}')

        global last_check_in
        last_check_in = datetime.now()
        self.title = '👨‍💻️'

    @rumps.clicked("💤 Check out")
    def check_out(self, _):
        shift_lenght = timedelta.total_seconds(datetime.now() - last_check_in)
        with open('timestamps.txt', 'a') as timestamps:
            timestamps.writelines(f'\nchecked out: {current_timestamp()}')
            timestamps.writelines(f'\n             {round(shift_lenght/60)} minutes total')
            timestamps.writelines(f'\n')

        self.title = "💤"

    @rumps.clicked("📘 Open report")
    def show_timestamps(self, _):
        os.system('open timestamps.txt')


CiCo("📘").run()
