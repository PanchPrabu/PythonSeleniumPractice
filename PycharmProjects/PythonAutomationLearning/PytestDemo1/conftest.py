import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be printing last")
@pytest.fixture()
def dataload():
    print("user profile is being created")
    return ["Panch","Prabu","panchatcharaprabu@gmail.com","Karaikudi"]

#@pytest.fixture(params=["Chrome","Firefox","IE"])
#def crossBrowser(request):
   # return request.param

@pytest.fixture(params=[("Chrome","Panch","Prabu"),("Firefox","Rahul"),("IE","Maha")])
def crossBrowser(request):
    return request.param
