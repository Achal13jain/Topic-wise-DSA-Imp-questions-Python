# Contributing Guide

Thank you for your interest in contributing to this DSA Practice Repository! 🎉

## How to Contribute

### Adding New Solutions

1. **Fork the repository** and create a new branch
2. **Add your solution** in the appropriate topic folder
3. **Follow the naming convention**: `problem_name.py`
4. **Include documentation**:
   ```python
   """
   Problem: [Problem Name]
   
   Approach: [Brief description of your approach]
   Time Complexity: O(...)
   Space Complexity: O(...)
   
   Example:
   Input: ...
   Output: ...
   """
   ```
5. **Test your code** with edge cases
6. **Submit a pull request** with a clear description

### Code Style Guidelines

- Use **descriptive variable names**
- Add **comments** for complex logic
- Follow **PEP 8** Python style guide
- Keep functions **modular and clean**
- Include **time and space complexity** analysis

### Important Problems (_IMP)

If you're adding an important interview problem:
- Suffix the filename with `_IMP` (e.g., `MaxSumSubArr_IMP.py`)
- Ensure the solution is **optimal**
- Include **multiple approaches** if applicable
- Add **detailed comments**

### Problem Structure

```python
"""
Problem: Problem Name Here
Topic: [Topic Name]

Approach:
- Describe your algorithm
- Mention time/space complexity
- Explain key insights

Time Complexity: O(n)
Space Complexity: O(1)
"""

def solution(input_data):
    """
    Detailed docstring explaining the function.
    
    Args:
        input_data: Description of input
    
    Returns:
        Description of output
    """
    # Implementation here
    pass


# Test cases
if __name__ == "__main__":
    # Example test case
    assert solution(test_input) == expected_output
    print("All tests passed!")
```

### Types of Contributions Welcome

- ✅ New problem solutions
- ✅ Alternative/optimized approaches
- ✅ Bug fixes in existing code
- ✅ Better explanations/comments
- ✅ Performance improvements
- ✅ Documentation improvements
- ✅ Test cases for existing problems

### What NOT to Do

- ❌ Don't add brute force solutions without optimization
- ❌ Don't skip time/space complexity analysis
- ❌ Don't add incomplete or untested code
- ❌ Don't duplicate existing solutions without significant improvement
- ❌ Don't add solutions in other languages (Python only)

## Pull Request Process

1. **Update your branch** with the latest main branch
2. **Ensure all code is tested** and working
3. **Write a clear PR title** and description
4. **Reference any related issues** (if applicable)
5. **Wait for review** - Maintainers will provide feedback if needed

## Reporting Issues

- Found a bug? Create an issue with:
  - Problem filename
  - Description of the issue
  - Expected vs actual behavior
  - Your environment (Python version, OS)

## Community

- Be respectful and constructive
- Help others learn and improve
- Share your knowledge freely
- Celebrate each contribution

## Questions?

Open an issue or discussion if you have questions about:
- Algorithm approaches
- How to solve a problem
- Code improvements
- Repository structure

---

Thank you for making this repository better! 🚀
