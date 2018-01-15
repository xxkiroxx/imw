from mysql import DB


class VirtualMachine:

    def __init__(self, id):
        self.db = DB("roberto", "78619841Ee.", "vmweb")
        sql = f"select * from vmachine where id={id}"
        print(sql)
        query = self.db.query(sql)
        self.id = query[0]["id"]
        self.name = query[0]["name"]
        self.ram = query[0]["ram"]
        self.cpu = query[0]["cpu"]
        self.hdd = query[0]["hdd"]
        self.os = query[0]["os"]
        self.status = query[0]["status"]

    def stop(self):
        sql = f"update vmachine set status=0 where id={self.id}"
        self.db.run(sql)
        sql = f"delete from process where vmachine_id={self.id}"
        self.db.run(sql)
        self.status = 0

    def start(self):
        sql = f"update vmachine set status=1 where id={self.id}"
        self.db.run(sql)
        self.status = 1

    def suspend(self):
        sql = f"update vmachine set status=2 where id={self.id}"
        self.db.run(sql)
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def run(self, pid, ram, cpu, hdd):
        sql = f"insert into process (pid, ram, cpu, hdd, vmachine_id) values ({pid},{ram},{cpu},{hdd}, {self.id})"
        self.db.run(sql)

    def get_processes(self):
        sql = f"select * from process where vmachine_id={self.id}"
        query = self.db.query(sql)
        return query

    def get_status(self):
        sql = f"select status from vmachine where id={self.id}"
        query = self.db.query(sql)
        status = query[0]["status"]
        if status == 0:
            return "Stopped"
        elif status == 1:
            return "Running"
        elif status == 2:
            return "Suspended"

    def ram_usage(self):
        ram = 0
        for p in self.get_processes():
            ram += p["ram"]
        percentage = ram * 100 / self.ram
        return round(percentage, 2)

    def cpu_usage(self):
        cpu = 0
        for p in self.get_processes():
            cpu += p["cpu"]
        percentage = cpu * 100 / self.cpu
        return round(percentage, 2)

    def hdd_usage(self):
        hdd = 0
        for p in self.get_processes():
            hdd += p["hdd"]
        percentage = hdd * 100 / self.hdd
        return round(percentage, 2)

    def __str__(self):
        return """
{} <{}> [{}]
{:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used
        """.format(
            self.os,
            self.name,
            self.get_status(),
            self.ram_usage(),
            self.cpu_usage(),
            self.hdd_usage()
        )
