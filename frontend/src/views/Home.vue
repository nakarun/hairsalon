<template>
  <div class="home">
    <GlobalHeader />
    <GlobalMessage />
    <main class="container mt-5 p-5">
      <Stamp />
      <Pointcards ref="pointcards"/>
      <CreatePointcard @created="fetchPointcards"/>
      <Posts ref="posts"/>
      <Post @posted="fetchPosts"/>
    </main>
  </div>
</template>

<script>
// @ is an alias to /src
import GlobalHeader from "@/components/GlobalHeader";
import GlobalMessage from "@/components/GlobalMessage";
import Stamp from "@/components/Stamp"
import Pointcards from "@/components/Pointcards"
import CreatePointcard from "@/components/CreatePointcard";
import Posts from "@/components/Posts"
import Post from "@/components/Post"

export default {
  name: "Home",
  components: {
    GlobalHeader,
    GlobalMessage,
    Stamp,
    Pointcards,
    CreatePointcard,
    Posts,
    Post
  },
  methods: {
    fetchPointcards() {
      this.$store.dispatch("pointcards/getPointcards", {
        salon: this.$store.state.salon.uuid,
      })
      .then(() => {
        console.log('get salon data ad pointcards.');
      })
    },
    fetchPosts() {
      this.$refs.posts.fetchItems();
    }
  },
  created: function () {
    // user.uuidからstaff情報を取得
    this.$store.dispatch("staff/getStaffData", {
      useruuid: this.$store.state.auth.useruuid,
    })
    .then(() => {
      // staff.salon.uuidからsalon情報を取得
      this.$store.dispatch("salon/getSalonData", {
        salon: this.$store.state.staff.salon,
      })
      .then(() => {
        // salonに紐づくポイントカードを取得
        this.fetchPointcards();
      })
    })
  },
};
</script>
