
import pytest
from unittest.mock import MagicMock
from faker import Faker
from paymentCode import PaymentService

# Initialize Faker
fake = Faker()

@pytest.fixture
def mock_notification_service():
    """Fixture to mock the notification service."""
    return MagicMock()

@pytest.fixture
def fake_user_data():
    """Fixture to generate fake user data using Faker."""
    return {
        "account_number": fake.random_int(min=1, max=9999),
        "amount_due": fake.random_number(digits=3)  # Random amount up to 999
    }

# Test mocking the notification service
def test_payment_success(mock_notification_service, fake_user_data):
    """Test successful payment processing with mocked notification."""
    service = PaymentService(notification_service=mock_notification_service)

    result = service.process_payment(fake_user_data['user_id'], fake_user_data['amount'])

    # Assert
    assert result == "Payment successful"
    mock_notification_service.send_notification.assert_called_once_with(
        fake_user_data['user_id'], f"Payment of {fake_user_data['amount']} is successful.")

# Stub method to process the transaction
def test_payment_transaction_stub(mock_notification_service):
    """Test payment processing using a stub for the transaction."""
    service = PaymentService(notification_service=mock_notification_service)

    # Stub returns False (simulate a failed payment)
    service._process_transaction = lambda user_id, amount: False

    result = service.process_payment(1, 100)

    # Assert
    assert result == "Payment failed"
    mock_notification_service.send_notification.assert_not_called()

# Test invalid payment amount with mocking
def test_invalid_payment_amount(mock_notification_service):
    """Test handling of invalid payment amount."""
    service = PaymentService(notification_service=mock_notification_service)

    result = service.process_payment(1, 0)

    # Assert
    assert result == "Invalid amount"
    mock_notification_service.send_notification.assert_not_called()