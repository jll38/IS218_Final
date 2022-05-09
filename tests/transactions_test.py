def test_transactions_deny(client):
    """test transactions access when not logged in"""
    response = client.get("/transactions")
    assert response.status_code == 302

def test_transactions_upload_deny(client):
    """test transactions upload page access when not logged in"""
    response = client.get("/transactions")
    assert response.status_code == 302

def test_transactions_csv_upload(client):
    fileName = "transactions.csv"
    data = {'csv': (open(fileName, 'rb'), fileName)}
    response = client.post("/transactions/upload", data=data)
    assert response.status_code == 400