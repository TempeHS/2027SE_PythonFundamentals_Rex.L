from jar import Jar


def test_default():
      jar = Jar()
      assert jar.capacity == 12
      assert jar.size == 0


def test_custom():
      jar = Jar(20)
      assert jar.capacity == 20


def test_empty():
      jar = Jar()
      assert str(jar) == ""


def test_str():
	jar = Jar()
	assert str(jar) == ""
	jar.deposit(1)
	assert str(jar) == "🍪"
	jar.deposit(11)
	assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_normal():
      jar = Jar()
      jar.deposit(5)
      assert jar.size == 5
    

def test_full():
      jar = Jar(5)
      jar.deposit(5)
      assert jar.size == 5
