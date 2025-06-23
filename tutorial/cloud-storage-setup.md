# Google Cloud Storage Setup for Gemini 2.5 Transcription

## Quick Start Guide

This guide helps you set up Google Cloud Storage for your Gemini 2.5 transcription workflow.

## Prerequisites

- Google Cloud Project with billing enabled
- Cloud Storage API enabled
- `gcloud` CLI installed (optional but recommended)

### Enable Cloud Storage API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **APIs & Services** > **Library**
3. Search for "Cloud Storage API"
4. Click **Enable**

## Method 1: Using Google Cloud Console (Beginner-Friendly)

### Step 1: Create a Storage Bucket

1. Go to [Google Cloud Storage](https://console.cloud.google.com/storage)
2. Click **Create Bucket**
3. Configure your bucket:
   - **Name**: Choose a globally unique name (e.g., `yourname-transcription-audio-2025`)
   - **Location Type**: Select "Region"
   - **Region**: Choose closest to you (e.g., `us-central1` for USA)
   - **Storage Class**: Select "Standard"
   - **Access Control**: Choose "Uniform" (recommended for transcription)
4. Click **Create**

### Step 2: Upload Audio Files

**Option A: Drag & Drop**
1. Open your newly created bucket
2. Drag your audio/video files directly into the browser
3. Wait for upload to complete

**Option B: Upload Button**
1. In your bucket, click **Upload Files**
2. Select your audio/video files
3. Click **Open**

### Step 3: Get the File URI

1. Click on your uploaded file
2. Copy the **gs://your-bucket-name/filename.ext** URI
3. Use this URI in your Gemini transcription code

## Method 2: Using Command Line (Advanced)

### Step 1: Install and Configure gcloud CLI

```bash
# Install gcloud CLI (if not already installed)
# Visit: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID
```

### Step 2: Create Bucket via CLI

```bash
# Create bucket
gsutil mb -p YOUR_PROJECT_ID -c STANDARD -l us-central1 gs://your-bucket-name

# Example:
gsutil mb -p my-transcription-project -c STANDARD -l us-central1 gs://my-transcription-bucket-2025
```

### Step 3: Upload Files via CLI

```bash
# Upload single file
gsutil cp /path/to/your/audio.m4a gs://your-bucket-name/

# Upload multiple files
gsutil cp /path/to/audio/*.m4a gs://your-bucket-name/

# Upload with parallel processing (faster for large files)
gsutil -m cp /path/to/audio/*.m4a gs://your-bucket-name/

# Upload entire directory
gsutil -m cp -r /path/to/audio-directory gs://your-bucket-name/
```

### Step 4: Verify Upload

```bash
# List files in bucket
gsutil ls gs://your-bucket-name/

# Get detailed info
gsutil ls -l gs://your-bucket-name/
```

## Supported Audio/Video Formats

✅ **Supported Formats:**
- **Audio**: WAV, MP3, M4A, AAC, FLAC, OGG, OPUS
- **Video**: MP4, MOV, AVI, WEBM

⚠️ **File Limits:**
- Maximum file size: 2GB per file
- Maximum audio length: ~9.5 hours per file
- For larger files, consider splitting them

## Best Practices

### 1. Bucket Naming

```bash
# Good naming examples:
gs://company-transcription-prod-2025
gs://myproject-audio-files-uscentral1
gs://interview-recordings-batch-001

# Avoid:
gs://my bucket  # No spaces
gs://MyBucket   # Avoid uppercase
gs://temp       # Too generic
```

### 2. Folder Organization

```bash
# Organize by date or project
gs://your-bucket/2025/01/january-interviews/
gs://your-bucket/projects/client-alpha/recordings/
gs://your-bucket/processed/transcripts/
gs://your-bucket/raw/incoming/
```

### 3. File Naming

```bash
# Good file names:
interview-2025-01-15-client-alpha.m4a
meeting-product-review-20250115.wav
podcast-episode-042-final.mp3

# Avoid:
my recording.m4a          # Spaces
interview@client!.wav     # Special characters
really-long-filename-that-is-hard-to-work-with.m4a  # Too long
```

## Cost Optimization Tips

### 1. Storage Classes

| Storage Class | Use Case | Cost |
|---------------|----------|------|
| **Standard** | Active transcription work | Higher storage, lower access |
| **Nearline** | Monthly access | Lower storage, higher access |
| **Coldline** | Quarterly access | Lowest storage, highest access |
| **Archive** | Yearly access or backup | Cheapest storage, expensive access |

### 2. Lifecycle Management

```bash
# Set lifecycle rules to automatically move old files
# Example: Move files older than 30 days to Nearline storage
```

**Via Console:**
1. Go to your bucket settings
2. Click **Lifecycle**
3. Add rule: "Move to Nearline after 30 days"

### 3. Monitor Usage

```bash
# Check storage usage
gsutil du -s gs://your-bucket-name/

# Check costs in Cloud Console
# Navigate to Billing > Cost breakdown
```

## Security Best Practices

### 1. Access Control

```bash
# Make bucket private (recommended)
gsutil iam ch -d allUsers:objectViewer gs://your-bucket-name

# Grant access to specific service account
gsutil iam ch serviceAccount:your-service-account@project.iam.gserviceaccount.com:objectViewer gs://your-bucket-name
```

### 2. Service Account Permissions

For Vertex AI transcription, your service account needs:
- `Storage Object Viewer` role on the bucket
- `Vertex AI User` role for transcription

## Troubleshooting

### Common Issues

**Issue: "Access Denied" when uploading**
```bash
# Solution: Check permissions
gsutil iam get gs://your-bucket-name
```

**Issue: "Bucket name already exists"**
```bash
# Solution: Bucket names are globally unique, try a different name
gsutil mb gs://your-project-transcription-unique-2025
```

**Issue: Files not appearing in Vertex AI**
```bash
# Solution: Verify the URI format
# Correct: gs://bucket-name/file.m4a
# Incorrect: https://storage.googleapis.com/bucket-name/file.m4a
```

**Issue: Slow uploads**
```bash
# Solution: Use parallel processing
gsutil -m cp -r /path/to/files gs://your-bucket-name/
```

## Integration with Transcription Code

Once your files are uploaded, use them in your Gemini code:

```python
# Example with proper URI
audio_part = Part.from_uri(
    uri="gs://your-bucket-name/interview.m4a",
    mime_type="audio/mp4"  # Use correct MIME type for m4a
)
```

### MIME Type Reference

| File Extension | MIME Type |
|----------------|-----------|
| .m4a | audio/mp4 |
| .mp3 | audio/mpeg |
| .wav | audio/wav |
| .flac | audio/flac |
| .ogg | audio/ogg |
| .mp4 | video/mp4 |
| .mov | video/quicktime |
| .avi | video/x-msvideo |

## Batch Processing Setup

For processing multiple files, organize them systematically:

```bash
# Create organized structure
mkdir -p audio-processing/{incoming,processing,completed,failed}

# Upload organized batches
gsutil -m cp audio-processing/incoming/*.m4a gs://your-bucket-name/batch-001/
gsutil -m cp audio-processing/incoming/*.wav gs://your-bucket-name/batch-002/
```

## Monitoring and Alerts

### Set up monitoring for your bucket:

1. Go to [Cloud Monitoring](https://console.cloud.google.com/monitoring)
2. Create alerts for:
   - Storage usage exceeding budget
   - Unusual access patterns
   - Failed uploads

### Example Alert Policy:

```yaml
# Alert when bucket size exceeds 10GB
condition:
  displayName: "Storage bucket size alert"
  conditionThreshold:
    filter: 'resource.type="gcs_bucket"'
    comparison: COMPARISON_GREATER_THAN
    thresholdValue: 10737418240  # 10GB in bytes
```

## Next Steps

1. ✅ Create your storage bucket
2. ✅ Upload sample audio file
3. ✅ Test with Gemini transcription code
4. ✅ Set up monitoring and alerts
5. ✅ Implement batch processing workflow

[← Back to Main Tutorial](../25-video-transcription-with-gemini-2-5.md)

---

**Need help?** Check the [troubleshooting section](#troubleshooting) or refer to the [Google Cloud Storage documentation](https://cloud.google.com/storage/docs).
