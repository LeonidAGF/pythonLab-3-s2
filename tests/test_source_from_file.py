from src.SourceFromFile import SourceFromFile


def test_source_from_file():
    """
        Тесты для SourceFromFile
    """
    sff1:SourceFromFile = SourceFromFile("./tests/test_cat_function.py",seed=555)
    sff2:SourceFromFile = SourceFromFile("./tests/test_cat_function.py",seed=555)
    sff3:SourceFromFile = SourceFromFile("./tests/test_cat_function.py")

    assert len(sff1.get_tasks())!=0
    assert len(sff2.get_tasks())!=0
    assert sff1.get_tasks()[0].id==sff2.get_tasks()[0].id
    assert len(sff3.get_tasks())!=0
