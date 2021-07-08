<template>
  <div class="post">
    <v-card>
      <v-card-title>お知らせを投稿する</v-card-title>
      <v-form
        class="pa-3"
        ref="form"
        v-model="valid"
        lazy-validation
        >
        <v-text-field
          v-model="title"
          :counter="10"
          :rules="titleRules"
          label="タイトル"
          required
        ></v-text-field>
        <v-textarea
          v-model="body"
          filled
          required
        ></v-textarea>
        <v-btn
          :disabled="!valid"
          color="primary"
          class="mt-4"
          block
          @click="validate"
        >
          投稿する
        </v-btn>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "Post",
  data: () => ({
    valid: true,
    title: '',
    titleRules: [
      v => !!v || 'タイトルを入力してください。',
      v => (v && v.length <= 10) || 'タイトルは10文字以内です。',
    ],
    body: '',
    bodyRules: [
      v => !!v || '本文を入力してください。',
      v => (v && v.length <= 100) || '本文は100文字以内です。',
    ],
  }),
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.submit();
      }
    },
    reset () {
      this.$refs.form.reset();
    },
    submit() {
      api.post('/news/', {
        title: this.title,
        body: this.body,
        published: new Date(),
      })
      .then(response => {
        console.log(`posted. ${response.data}`);
        this.$emit("posted");
        this.reset();
      })
      .catch(function(error) {
        console.log(error);
      })
    },
  }
}
</script>

<style scoped>
.post {
  padding: 10px;
}
</style>