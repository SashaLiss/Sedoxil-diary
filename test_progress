from sedoxil_diary import progress

## A function to get a progress in the timeline of treatment - a part of sedoxil_diary program - here to test the inputs##
# this test can be run with pytest.

def main():
    test_progress()

def test_progress():

    assert progress('1950/09/04', '2023/03/02', 5) == False
    assert progress('2023/03/01', '2023/03/02', 5) == (2,3)
    assert progress('2023/02/10', '2023/03/02', 30) == (21,9)




if __name__ == "__main__":
    main()
