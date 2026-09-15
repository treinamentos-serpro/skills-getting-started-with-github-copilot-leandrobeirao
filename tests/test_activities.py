def test_get_activities_returns_available_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == 9
    assert expected_activity in activities
    assert activities[expected_activity]["max_participants"] == 12


def test_root_redirects_to_static_index(client):
    # Arrange
    redirect_options = {"follow_redirects": False}

    # Act
    response = client.get("/", **redirect_options)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"