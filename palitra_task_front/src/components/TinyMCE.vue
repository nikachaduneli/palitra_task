<script setup>

import Editor from '@tinymce/tinymce-vue'
import axios from 'axios'

const handleImageUpload = async (blobInfo, progress, failure) => {
  const formData = new FormData();
  formData.append("file", blobInfo.blob(), blobInfo.filename());

  try {
    const response = await axios.post(
        "http://localhost:8000/server.php",
        formData,
        {
          headers: {"Content-Type": "multipart/form-data"},
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
            );
            if (progress && typeof progress === "function") {
              progress(percentCompleted);
            }
          },
        }
    );

    if (response.status === 403) {
      throw new Error("HTTP Error: " + response.status);
    }

    if (response.status < 200 || response.status >= 300) {
      throw new Error("HTTP Error: " + response.status);
    }

    const json = response.data;

    if (!json || typeof json.location !== "string") {
      throw new Error("Invalid JSON: " + JSON.stringify(json));
    } else response;
    {
      return json.location;
    }
  } catch (error) {
    if (failure && typeof failure === "function") {
      failure(error.message);
    }
  }
};

</script>

<template>
  <Editor
      api-key="zs45ez3dxnwlgn7jyt7zjz66ijjryajr86zgf4l7jm3tzue8"
      :init="{
        menubar: false,
        plugins: 'lists link image emoticons',
        toolbar: 'styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist | link image emoticons',
        images_upload_url: 'http://localhost:8000/server.php',
        automatic_uploads: true,
        images_reuse_filename: true,
        images_upload_handler: handleImageUpload,
      }"
  />
</template>

<script>
export default {
  name: 'TinyMCE',
  props: {}
}
</script>