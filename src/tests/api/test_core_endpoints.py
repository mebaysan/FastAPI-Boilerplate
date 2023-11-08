def test_endpoint_healthcheck(client, app_settings):
    """Tests the healthcheck endpoint."""
    response = client.get("healthcheck/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app_name": app_settings.app_name}
