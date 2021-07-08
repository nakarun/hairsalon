<template>
  <div class="create-pointcard">
    <v-card>
      <v-card-title>ポイントカードを追加する</v-card-title>
      <v-form
        class="pa-3"
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="v"
          type="number"
          label="縦の枠数を入力してください。"
        >
        </v-text-field>
        <v-text-field
          v-model="h"
          type="number"
          label="横の枠数を入力してください。"
        >
        </v-text-field>
        <v-btn
          :disabled="!valid"
          color="primary"
          class="mt-4"
          block
          @click="validate"
        >
          作成する
        </v-btn>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "CreatePointcard",
  data: () => ({
    valid: true,
    v: 0,
    h: 0,
  }),
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.createPointcard();
      }
    },
    reset () {
      this.$refs.form.reset();
    },
    createPointcard() {
      const salon = this.$store.state.salon.uuid;
      api.post('/pointcard/', {
        salon: salon,
        vertical_cells_count: this.v,
        horizontal_cells_count: this.h,
      })
      .then(response => {
        console.log(response)
        this.$emit('created');
        this.reset();
      })
      .catch(function(error) {
        console.log(error)
      })
    },
  },
}
</script>

<style scoped>
.create-pointcard {
  padding: 10px;
}
</style>