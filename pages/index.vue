<template>
  <div class="page-index d-f fd-c ai-c">
    <TheTop />
    <TheInclude />
    <TheBenefit />
    <TheStep />
    <TheFormCalculate
      :price="price"
      @check-calculate-prop="checkCalculate"
      @fetch-calculate="fetchCalculate"
    />
    <TheFormOrder
      :is-enabled="isFormOrderEnabled"
      :is-same-data="isSameData"
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
    calculateData: {},
    calculateDataAfter: {
      accident_death: null,
      accident_disability: null,
      count_days: null,
      is_professional: null,
      is_sporttime: null,
      promo: null,
      timedisability_accident: null,
      type_of_sport: null,
    },
  }),
  computed: {
    isFormOrderEnabled() {
      return !!this.price;
    },
    isSameData() {
      if (!this.isFormOrderEnabled) {
        return true;
      }
      for (const prop in this.calculateData) {
        const valueAfter = JSON.stringify(this.calculateDataAfter[prop]);
        const value = JSON.stringify(this.calculateData[prop]);
        if (valueAfter !== value) {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    checkCalculate(prop, value) {
      if (!this.isFormOrderEnabled) {
        return;
      }
      this.calculateDataAfter[prop] = value;
    },
    async fetchCalculate(data) {
      this.calculateDataAfter = { ...data };
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
