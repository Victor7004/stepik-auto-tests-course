#incoding: cp866
def test_substring(full_string, substring):
    assert substring in full_string,\
    f"expected '{substring}' to be substring of '{full_string}'"
    # ���� ����������, �������� assert � ��������� �� ������


test_substring('111', '44')