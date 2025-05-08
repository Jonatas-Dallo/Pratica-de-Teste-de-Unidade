import pytest
from src.custom_stack_class import *

def test_push_one_elementinstack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    assert not cut.is_empty()
    assert cut.top() == element_value
    assert cut.size() == 1

def test_push_until_full_raises_exception():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(StackFullException):
        stack.push(3)

def test_pop_from_empty_stack_raises_exception():
    stack = CustomStack(2)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top_from_empty_stack_raises_exception():
    stack = CustomStack(2)
    with pytest.raises(StackEmptyException):
        stack.top()

def test_push_and_pop_sequence():
    stack = CustomStack(3)
    stack.push('a')
    stack.push('b')
    assert stack.top() == 'b'
    assert stack.pop() == 'b'
    assert stack.top() == 'a'
    assert stack.size() == 1

# ----------------------------------------------- #

def test_sort_stack_with_six_numbers():
    stack = CustomStack(6)
    numbers = [45, 2, 33, 17, 8, 50]

    for n in numbers:
        stack.push(n)

    sorter = NumberAscOrder()
    result = sorter.sort(stack)

    assert result == sorted(numbers)
    assert stack.is_empty()

def test_sort_empty_stack_raises_error():
    stack = CustomStack(6)
    sorter = NumberAscOrder()

    with pytest.raises(ValueError, match="Pilha está vazia"):
        sorter.sort(stack)
