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
      @post-buy="postBuy"
      @post-getdraft="postGetdraft"
    />
    <TheQuestion />
  </div>
</template>

<script>
import errorsMixin from '~/mixins/errors';
import { base64ToArrayBuffer, downloadBlob } from '~/helpers/pdf';
import {
  postSaveAction,
  postBuyAction,
  postGetdraftAction,
} from '~/api/api';
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

    async postGetdraft(formData) {
      const body = {
        ...this.calculateData,
        ...formData,
      }
      const res = await postSaveAction(this, { body })
        .catch(this.actionFail)

      if (!res) {
        return;
      }

      return postGetdraftAction(this, { body: res.data })
        .then(this.postGetdraftSuccess)
        .catch(this.actionFail);
    },
    postGetdraftSuccess(response) {
      const pdf = base64ToArrayBuffer(response.data.total);
      downloadBlob(pdf, 'Предпросмотр договора страхования.pdf', 'application/pdf');
    },

    async postBuy(formData) {
      const body = {
        ...this.calculateData,
        ...formData,
      }
      const res = await postSaveAction(this, { body })
        .catch(this.actionFail)

      if (!res) {
        return;
      }

      return postBuyAction(this, { body: res.data })
        .then(this.postBuySuccess)
        .catch(this.actionFail);
    },
    postBuySuccess({ data }) {
      window.open(data.total, '_self');
    },
  },
}
</script>

<style lang="scss">
</style>
