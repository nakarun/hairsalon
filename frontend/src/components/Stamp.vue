<template>
  <div class="stamp">
    <v-card>
      <v-card-title>スタンプを発行する</v-card-title>
      <v-form
        class="pa-3"
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-select
          v-model="selectedPointcard"
          :items="pointcards"
          label="ポイントカードを選択する"
          item-text="uuid"
          attach
          :menu-props="{ top: false, offsetY: true }"
          return-object
        >
        </v-select>
        <v-select
          v-model="selectedCustomer"
          :items="customers"
          label="利用者を選択する"
          item-text="username"
          attach
          :menu-props="{ top: false, offsetY: true }"
          return-object
        >
        </v-select>
        <v-date-picker v-model="picker"></v-date-picker>
        <v-btn
          :disabled="!valid"
          color="primary"
          class="mt-4"
          block
          @click="validate"
        >
          スタンプを押す
        </v-btn>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "Stamp",
  data: () => ({
    valid: true,
    picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    customers: [],
    selectedCustomer: {},
    selectedPointcard: {},
  }),
  computed: {
    pointcards: function () {
      return this.$store.state.pointcards.pointcards;
    },
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.submit();
      }
    },
    reset () {
      this.$refs.form.reset();
    },
    submit () {
      api.post('/stamp/', {
        customer: this.selectedCustomer.uuid,
        pointcard: this.selectedPointcard.uuid,
        stamped_at: this.picker,
      })
      .then(response => {
        console.log(response);
        this.reset();
      }).catch( function (error) {
        console.log(error);
      });
    },
    fetchCustomers () {
      api.get('/customer/')
      .then(response => {
        this.customers = response.data;
      })
      .catch(function(error) {
        console.log(error);
      });
    }
  },
  created: function () {
    this.fetchCustomers();
  }
}
</script>

<style scoped>
.stamp {
  padding: 10px;
}
</style>