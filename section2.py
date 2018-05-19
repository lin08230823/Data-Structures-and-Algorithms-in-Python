import datetime


class PersonTypeError(TypeError):
	pass

class PersonValueError(ValueError):
	pass
#公共人员类的实现
class Person(object):
	"""docstring for Person"""
	_num = 0

	def __init__(self, name, sex, birthday, ident):
		if not (isinstance(name, str) and 
			sex in ('男', '女'):
			raise PersonValueError(name, sex)
		try:
			birth = datetime.date(*birthday)
		except:
			raise PersonValueError("Wrong date:", birthday)
		self._name = name
		self._sex = sex
		self._birthday = birth
		self._id = ident
		Person._num += 1

	def id(self):
		return self._id

	def name(self):
		return self._name

	def sex(self):
		return self._sex

	def birthday(self):
		return self._birthday

	def age(self):
		return (datetime.date.today().year - self._birthday.year)

	def set_name(self, name):
		if not isinstance(name, str):
			raise PersonValueError("set_name": name)
		self._name = name

	def __lt__(self, another):
		if not isinstance(another, Person)
			raise PersonTypeError(another)
		return self._id < another._id

	@classmethod
	def num(cls):
		return cls._num

	def __str__(self):
		return " ".join(self._id, self._name, self._sex, str(self._birthday))

	def details(self):
		return " ".join(("编号： " + self._id,
						 "姓名： " + self._name,
						 "性别： " + self._sex,
						 "出生日期： " + str(self._birthday
			))

p1 = Person("谢玉洁"， "女"，(1995, 7, 30), "1201510111")
p2 = Person("王立群"， "男", (1990, 2, 17), "1201380324")

class Student(Person):
	_id_num = 0
	@classmethod
	def _id_gen(cls):  #实现学号生成规则
		cls._id_num += 1
		year = datatime.date.today().year
		return "1{:04}{:05}".format(year, cls._id_num)

	def __init__(self, name, sex, birthday, department):
		Person.__init__(self, name, sex, birthday, Student._id_gen())
		self._department = department
		self._enroll_date = datetime.date.today()
		self._courses = {}

	def set_course(self, course_name):
		self._courses[course_name] = None

	def set_score(self, course_name, score):
		if course_name not in self._courses:
			raise PersonValueError("No this course selected:",
									course_name)
		self._courses[course_name] = score

	def get_scores(self):
		return [(cname, self._courses[cname])
				for cname in self._courses]

	def detail(self):
		return ", ".join((Person.details(self),
						"入学日期: " + str(self._enroll_date),
						"院系: "+ self._department,
						"课程记录: " + str(self.get_scores())))
		
