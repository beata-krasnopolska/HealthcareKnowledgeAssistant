from app.core.settings import settings

def test_settings_loaded():
    assert settings is not None
    assert isinstance(settings.app_name, str)
    assert settings.app_name != ""