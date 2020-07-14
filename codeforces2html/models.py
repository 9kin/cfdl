import os

from peewee import *

dir_path = os.path.dirname(os.path.realpath(__file__))

db = SqliteDatabase(f"{dir_path}/cf.sqlite")


class Tasks(Model):

    id = CharField(max_length=15)
    name = CharField(max_length=100)  # название
    contest_title = CharField(max_length=100)

    condition = TextField()  # условие
    tutorial = TextField()  # разбор
    solution = TextField()  # решение
    tags = TextField()  # теги задачи

    materials = None

    class Meta:

        database = db
        db_table = "codeforces"


class Solutions(Model):
    solution_id = CharField(max_length=100)  # 1358F[1/2/3]
    solution = TextField()  # решение

    class Meta:

        database = db
        db_table = "solutions"


class Tutorials(Model):
    tutorial_id = CharField(max_length=100)  # 1358F[1/2/3]
    tutorial = TextField()  # идяе решения

    class Meta:

        database = db
        db_table = "tutorial"


class SolutionsArray:
    # parse_blog return string for sql (for fast query)
    # Solutions.select().where(Solutions.solution_id.startswith('1361A'))
    # key : string '1361A' val: '1361A[0],...'

    def __init__(self, array, urls={}):
        self.m = {}
        self.urls = urls
        for model in array:
            s = model["solution_id"][: model["solution_id"].find("[")]
            if s not in self.m:
                self.m[s] = [model]
            else:
                self.m[s].append(model)

    def __getitem__(self, key):
        if key in self.m:
            return self.m[key]
        else:
            return []

    def __str__(self):
        return str(len(self.m))

    def update(self, problemcode, submition):
        if problemcode not in self.m:
            self.m[problemcode] = [
                {"solution_id": problemcode + "[0]", "solution": submition}
            ]
        else:
            self.m[problemcode].append(
                {
                    "solution_id": f"{problemcode}[{len(self.m[problemcode])}]",
                    "solution": submition,
                }
            )
        # pprint(self.m[problemcode][-1])

    def get_array(self):
        # from pprint import pprint

        array = []
        for problemcode in self.m:
            for model in self.m[problemcode]:
                array.append(model)
                # pprint(model)

        return array


def clean_database():
    db.drop_tables([Tasks, Solutions])
    db.create_tables([Tasks, Solutions])


def refresh(ALL_TASKS, ALL_SOLUTIONS):
    Tasks.delete().where(
        Tasks.id << [task["id"] for task in ALL_TASKS]
    ).execute()
    Solutions.delete().where(
        Solutions.solution_id
        << [solution["solution_id"] for solution in ALL_SOLUTIONS]
    ).execute()

    # from pprint import pprint

    # for i in ALL_SOLUTIONS:
    #    pprint(i)
    # exit(0)
    with db.atomic():
        for batch in chunked(ALL_SOLUTIONS, 100):
            Solutions.insert_many(batch).execute()

    with db.atomic():
        for batch in chunked(ALL_TASKS, 100):
            Tasks.insert_many(batch).execute()


if __name__ == "__main__":
    clean()
