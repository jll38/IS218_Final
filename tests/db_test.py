import os


def test_create_database():
    """test database"""
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    assert os.path.exists(dbdir)