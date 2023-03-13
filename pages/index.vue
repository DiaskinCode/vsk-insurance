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
    <TheFormOrder />
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
  }),
  computed: {},
  methods: {
    async fetchCalculate(data) {
      const { response, fail } = await this.fetchCalculateAction(data);
      if (fail) {
        this.showError({ detail: response.data });
        return;
      }
      this.showSuccess({ detail: 'Стоимость полиса рассчитана' });
      this.price = Number(response.data.total);
    },
    async fetchCalculateAction(data) {
      const responseObject = await this.$axios.post('calculator/', data)
        .then((response) => ({ response, fail: false }))
        .catch((response) => ({ response, fail: true }));
      return responseObject;
    },
  },
}
</script>

<style lang="scss">
</style>
