from conversor import decimal_binario,binario_decimal

def test_decimal_binario():
    assert decimal_binario(25) == "11001"
    assert decimal_binario(13) == "1101"
    print(":D  decimal_binario paso los tests")


def test_binario_decimal():
    assert binario_decimal("11001") == 25
    assert binario_decimal("1101") == 13
    print(":D binario_decimal paso los tests")    

test_binario_decimal()
test_decimal_binario()