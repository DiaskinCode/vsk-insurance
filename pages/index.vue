<template>
  <div class="page-index d-f fd-c ai-c">
    <TheTop />
    <TheInclude />
    <TheBenefit />
    <TheStep />
    <TheFormCalculate
      :price="price"
      @fetch-calculate="fetchCalculate"
    />
    <TheFormOrder
      :is-enabled="isFormOrderEnabled"
      @fetch-order="fetchSave"
    />
    <TheQuestion />
  </div>
</template>

<script>
import errorsMixin from '~/mixins/errors';
export default {
  name: 'PageIndex',
  mixins: [
    errorsMixin,
  ],
  props: {},
  data: () => ({
    price: null,
    calculateData: null,
  }),
  computed: {
    isFormOrderEnabled() {
      return !!this.price;
    },
  },
  methods: {
    async fetchCalculate(data) {
      const { response, fail } = await this.fetchCalculateAction(data);
      if (fail) {
        this.showError({ detail: response.data });
        return;
      }
      this.showSuccess({ detail: 'Стоимость полиса рассчитана' });
      this.price = Number(response.data.total) / 100;
      this.calculateData = { ...data };
    },
    async fetchCalculateAction(data) {
      const responseObject = await this.$axios.post('calculator/', data)
        .then((response) => ({ response, fail: false }))
        .catch((response) => ({ response, fail: true }));
      return responseObject;
    },

    async fetchSave(data) {
      const { response, fail } = await this.fetchSaveAction(data);
      if (fail) {
        this.showError({ detail: response.data });
        return;
      }
      this.showSuccess({
        summary: 'Заявка оформлена',
        detail: 'Дальнейшие инструкции придут вам на почту',
      });
    },
    async fetchSaveAction(data) {
      const formData = { ...data, ...this.calculateData };
      const responseObject = await this.$axios.post('save/', formData)
        .then((response) => ({ response, fail: false }))
        .catch((response) => ({ response, fail: true }));
      return responseObject;
    },
  },
}
</script>

<style lang="scss">
</style>
