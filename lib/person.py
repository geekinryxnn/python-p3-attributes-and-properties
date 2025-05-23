#!/usr/bin/env python3

# lib/person.py

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    # --- Name property ---
    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # --- Job property ---
    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)

if __name__ == '__main__':
    person1 = Person(name="john doe", job="Sales")
    print(f"Person's name: {person1.name}")
    print(f"Person's job: {person1.job}")

    person1.name = ""
    person1.job = "Astronaut"