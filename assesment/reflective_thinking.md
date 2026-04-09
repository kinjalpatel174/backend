# Reflective Thinking: EduTracker Solutions API

## 1. How would you add real-time notifications (e.g., when a student enrolls)?
To implement real-time notifications in this Django project, I would follow these steps:
- **Django Channels:** Integrate Django Channels to handle WebSockets.
- **WebSocket Consumer:** Create a consumer that manages WebSocket connections for clients (e.g., an admin dashboard).
- **Signals:** Use Django `post_save` signals on the `Student` model. Whenever a new student is created, the signal would trigger a message through the Channel Layer to the connected WebSocket clients.
- **Frontend Integration:** Use the browser's `WebSocket` API to listen for these messages and display a toast notification to the user.

## 2. How would you allow video course uploads with file size limits?
For handling video uploads effectively:
- **Model Field:** Add a `FileField` or `ImageField` to the `Course` model.
- **Custom Validator:** Write a custom validator that checks `file.size`.
  ```python
  def validate_file_size(value):
      limit = 50 * 1024 * 1024 # 50 MB
      if value.size > limit:
          raise ValidationError('File too large. Size should not exceed 50 MB.')
  ```
- **Storage:** Instead of storing videos on the local server, use **Cloud Storage** like AWS S3 or Google Cloud Storage using `django-storages`.
- **Background Processing:** For very large videos, I would use **Celery** to handle transcoding or processing in the background to avoid blocking the request-response cycle.

## 3. How would you handle rate-limiting for high traffic from frontend/mobile?
Django REST Framework has robust built-in throttling mechanisms:
- **Global Throttling:** Configure rate limits in `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_THROTTLE_CLASSES': [
          'rest_framework.throttling.AnonRateThrottle',
          'rest_framework.throttling.UserRateThrottle'
      ],
      'DEFAULT_THROTTLE_RATES': {
          'anon': '100/day',
          'user': '1000/day'
      }
  }
  ```
- **Scoped Throttling:** For high-traffic endpoints (like searching), use `ScopedRateThrottle` to apply specific limits to those views only.
- **Cache Backend:** Use **Redis** as the cache backend for throttling to ensure performance and accuracy across multiple server instances.
