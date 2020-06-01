from scheduler import Scheduler
from eddystone import Broadcaster
from observer import Observer


def main():
    print("---Band is starting!---")
    scheduler = Scheduler()
    eddystone_sender = Broadcaster('https://thu-band.org')
    eddystone_scanner = Observer('https://thu-band.org')
    try:
        scheduler.run(eddystone_sender, eddystone_scanner)
    except:
        return


if __name__ == "__main__":
    main()
