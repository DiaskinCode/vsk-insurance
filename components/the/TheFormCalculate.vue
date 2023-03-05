<template>
  <div
    id="calculate"
    class="form-calculate container-wrapper bg-g"
  >
    <div class="container fd-c ai-c py-100 py-50-mb">
      <h2 class="header-text">
        Страхование несчастных случаев
      </h2>
      <div class="w-100 px-100 px-0-mb">
        <AppForm
          class="w-100 bg-w bs-1 br-30 p-55"
          ref="observer"
          :gy="50"
          :gy-mb="25"
          @submit="validateForm"
        >
          <div>
            <div class="fw-6 fs-25 lh-140 mb-15 ws-nw">
              Срок страхования
            </div>
            <AppFormField
              class="px-20"
              vid="term"
            >
              <AppSlider
                id="term"
                v-model="data.term"
                :min="1"
                :max="365"
              />
            </AppFormField>
          </div>
        </AppForm>
      </div>
    </div>
    <ClientOnly>
      <Teleport
        to=".form-calculate .p-slider-handle"
      >
        <div class="form-calculate__term bg-w b-1 br-5 py-10 d-f jc-c">
          {{ termString }}
        </div>
      </Teleport>
    </ClientOnly>
  </div>
</template>

<script>
export default {
  name: 'TheFormCalculate',
  props: {},
  data: () => ({
    loading: false,
    data: {
      term: 1,
      risks: '',
      sport: '',
      promo: '',
      professional: false,
      partner: false,
      rules: false,
    },
  }),
  computed: {
    termString() {
      const div = (val, by) => {
        return (val - val % by) / by;
      }
      const mod = (val, by) => {
        return val % by;
      }

      if (
        div(mod(this.data.term, 100), 10) === 1 ||
        mod(this.data.term, 10) > 4 ||
        mod(this.data.term, 10) === 0
      ) {
        return `${this.data.term} дней`;
      }
      if (mod(this.data.term, 10) > 1) {
        return `${this.data.term} дня`;
      }
      return `${this.data.term} день`;
    },
  },
  methods: {
    async validateForm() {
      const isValidForm = await this.$refs.observer.validate();
      if (!isValidForm) {
        return;
      }
      this.$emit('fetch-order', this.data);
    },
  },
}
</script>

<style lang="scss">
.form-calculate {
  /* .form-calculate__term */
  &__term {
    position: absolute;
    white-space: nowrap;
    border-color: #D2D2D2;
    width: 13rem;
    transform: translateX(-40%);
    top: -5rem;
  }
  .app-slider {
    color: #444444;
    &::before {
      position: absolute;
      left: 0;
      top: 2rem;
      transform: translateX(-50%);
      content: '1 день';
    }
    &::after {
      position: absolute;
      right: 0;
      top: 2rem;
      transform: translateX(50%);
      content: '365 дней';
    }
  }
  .p-slider-handle {
    &::before {
      position: absolute;
    }
  }
}
</style>
