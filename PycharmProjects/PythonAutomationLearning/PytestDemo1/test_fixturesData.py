import pytest

from PytestDemo1.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editprofile(self,dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload)
