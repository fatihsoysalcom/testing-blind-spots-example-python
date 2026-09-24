def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    This initial version has a 'blind spot' for empty lists.
    """
    # Developer's initial assumption: 'numbers' will always be non-empty.
    # This line will cause a ZeroDivisionError if 'numbers' is empty,
    # demonstrating a common 'blind spot' in development.
    return sum(numbers) / len(numbers)

def run_tests():
    """
    Runs a series of tests to demonstrate how developer's assumptions
    can create blind spots in testing.
    """
    print("--- Running Tests for calculate_average function ---")
    print("These tests reflect a developer's typical mental model,")
    print("assuming valid, non-empty inputs.
")

    try:
        # --- Tests reflecting common, expected scenarios ---
        # These tests pass because they align with the developer's initial assumptions.

        # Test Case 1: Positive integers
        result = calculate_average([1, 2, 3])
        assert result == 2.0, f"Test 1 Failed: Expected 2.0, got {result}"
        print("✅ Test 1 (Positive integers) passed.")

        # Test Case 2: Mixed integers (including zero and negatives)
        result = calculate_average([-1, 0, 1])
        assert result == 0.0, f"Test 2 Failed: Expected 0.0, got {result}"
        print("✅ Test 2 (Mixed integers) passed.")

        # Test Case 3: Floating point numbers
        result = calculate_average([1.5, 2.5])
        assert result == 2.0, f"Test 3 Failed: Expected 2.0, got {result}"
        print("✅ Test 3 (Floating point numbers) passed.")

        print("
--- Attempting to run a 'blind spot' test case ---")
        # --- The 'blind spot' test case ---
        # This test case represents an edge scenario or an unexpected input
        # that might be overlooked during initial test writing.
        # It is designed to expose a flaw that the previous tests didn't catch.
        result = calculate_average([])
        # If the function were fixed to handle empty lists (e.g., return None or raise ValueError),
        # this assert would check that. For this demo, we expect it to crash.
        print("❌ Blind spot test (Empty list) passed unexpectedly or did not crash.")
        print("   This indicates the function might have an unexpected behavior for empty lists.")

    except ZeroDivisionError:
        # This exception demonstrates the 'blind spot' being revealed.
        print("\n🛑 Blind spot test (Empty list) REVEALED a ZeroDivisionError!")
        print("   This error shows that the initial tests, based on the developer's")
        print("   mental model, failed to cover the edge case of an empty list.")
        print("   The function `calculate_average` does not handle this scenario gracefully.")
    except Exception as e:
        print(f"\n🛑 An unexpected error occurred during testing: {type(e).__name__} - {e}")

    print("\n--- All tests completed. ---")

if __name__ == "__main__":
    run_tests()