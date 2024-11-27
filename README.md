# Repro for issue 7998

## Versions

firebase-tools: v13.27.0<br>
node: v20.18.0<br>
platform: macOS Sonoma 14.7.1

## Steps to reproduce

1. Install dependencies
   - Run `cd py-codebase`
   - Run `python3.12 -m venv venv`
   - Run `. "./venv/bin/activate" && python3.12 -m pip install -r requirements.txt`
2. Run `firebase emulators:start --project demo-project`
3. Open "http://localhost:4000/firealerts"
   - Select "crashlytics.newNonfatalIssue"
   - Click "Send Alert"
   - Outputs:

```
Received event at channel google: {
  "alerttype": "crashlytics.newNonfatalIssue",
  "id": "34062873154104434",
  "source": "//firebasealerts.googleapis.com/projects/1234567890",
  "specVersion": "1.0",
  "appid": "1:1234567890:web:c3c43fe6995ba2a40d6192dcf84d83c",
  "time": "2024-11-27T13:16:25.328Z",
  "type": "google.firebase.firebasealerts.alerts.v1.published",
  "project": "1234567890",
  "data": {
    "@type": "type.googleapis.com/google.events.firebase.firebasealerts.v1.AlertData",
    "createTime": "2024-11-27T13:16:25.328Z",
    "endTime": "2024-11-27T13:16:25.328Z",
    "payload": {
      "@type": "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsNewNonfatalIssuePayload",
      "issue": {
        "appVersion": "1 (1.0.0)",
        "id": "1",
        "title": "TestApp.main",
        "subtitle": "Runtime Error"
      }
    }
  }
}
i  functions: Beginning execution of "us-central1-post_nonfatal_issue_py"
i  functions: Finished "us-central1-post_nonfatal_issue_py" in 2.541625ms
i  Failed to trigger Functions emulator for us-central1-post_nonfatal_issue_py-0: FirebaseError: Received non-200 status code: 415
```

## Notes

There are no issues when using a JavaScript codebase

1. Modify the `firebase.json` to use the `js-codebase`:

```json
{
  "functions": [
    {
      "source": "js-codebase",
      "codebase": "default",
      "ignore": [
        "venv",
        ".git",
        "firebase-debug.log",
        "firebase-debug.*.log",
        "*.local"
      ]
    }
  ]
}
```

2. Install dependencies
   - Run `cd js-codebase`
   - Run `npm i`
3. Run `firebase emulators:start --project demo-project`
4. Open "http://localhost:4000/firealerts"
   - Select "crashlytics.newNonfatalIssue"
   - Click "Send Alert"
   - Outputs:

```
Received event at channel google: {
  "alerttype": "crashlytics.newNonfatalIssue",
  "id": "5579364184687157",
  "source": "//firebasealerts.googleapis.com/projects/1234567890",
  "specVersion": "1.0",
  "appid": "1:1234567890:web:2f62f33c67f5ad1abfbfbe34c3d9a98e",
  "time": "2024-11-27T13:08:08.396Z",
  "type": "google.firebase.firebasealerts.alerts.v1.published",
  "project": "1234567890",
  "data": {
    "@type": "type.googleapis.com/google.events.firebase.firebasealerts.v1.AlertData",
    "createTime": "2024-11-27T13:08:08.396Z",
    "endTime": "2024-11-27T13:08:08.396Z",
    "payload": {
      "@type": "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsNewNonfatalIssuePayload",
      "issue": {
        "appVersion": "1 (1.0.0)",
        "id": "1",
        "title": "TestApp.main",
        "subtitle": "Runtime Error"
      }
    }
  }
}
i  functions: Beginning execution of "us-central1-post_nonfatal_issue_js"
>
>      🚨 New fatal issue for 1:1234567890:web:2f62f33c67f5ad1abfbfbe34c3d9a98e in version 1 (1.0.0) 🚨
>
>      **TestApp.main**
>
>      Runtime Error
>
>      id: `1`
>
i  functions: Finished "us-central1-post_nonfatal_issue_js" in 10.6545ms
```
