<template>
  <div class="home">
    <PostInfo />
  </div>
</template>

<script>
// @ is an alias to /src
import PostInfo from "@/components/PostInfo"

export default {
  name: "Home",
  components: {
    PostInfo,
  },
};
</script>
