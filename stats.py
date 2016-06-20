import luigi
from alerts import GenerateAlertsTask
from utils import clean_files

class GenerateStatsTask(luigi.Task):
    task_namespace = 'stats'

    def requires(self):
        return GenerateAlertsTask()

    def run(self):
        print("{task} says: ready to generate stats!".format(task=self.__class__.__name__))
        clean_files()
