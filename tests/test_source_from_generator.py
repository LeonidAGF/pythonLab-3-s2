from src.SourceFromGenerator import SourceFromGenerator


def test_source_from_generator():
    """
        Тесты для SourceFromGenerator
    """
    sfg1: SourceFromGenerator = SourceFromGenerator(1, seed=555)
    sfg3: SourceFromGenerator = SourceFromGenerator(2)
    sfg4: SourceFromGenerator = SourceFromGenerator(3)
    sfg5: SourceFromGenerator = SourceFromGenerator(4)
    sfg6: SourceFromGenerator = SourceFromGenerator(5)

    try:
        SourceFromGenerator(6)
        assert False
    except Exception:
        assert True

    assert len(sfg1.get_tasks()[0].payload.get('numbers',[])) != 0
    assert len(sfg3.get_tasks()[0].payload.get('numbers',[])) != 0
    assert len(sfg4.get_tasks()[0].payload.get('numbers',[])) != 0
    assert len(sfg5.get_tasks()[0].payload.get('numbers',[])) != 0
    assert len(sfg6.get_tasks()[0].payload.get('numbers',[])) != 0
