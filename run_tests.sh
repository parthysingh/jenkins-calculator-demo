#!/bin/bash

echo "=========================================="
echo "Jenkins Automated Testing Demo"
echo "=========================================="
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt --break-system-packages --quiet

echo ""
echo "Running Unit Tests..."
echo "=========================================="

# Run tests with pytest and generate coverage report
python3 -m pytest tests/ -v --tb=short --cov=src --cov-report=html --cov-report=xml --cov-report=term

TEST_EXIT_CODE=$?

echo ""
echo "=========================================="
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed successfully!"
else
    echo "❌ Some tests failed!"
fi
echo "=========================================="

# Generate JUnit XML for Jenkins
python3 -m pytest tests/ --junitxml=test-results.xml

exit $TEST_EXIT_CODE
