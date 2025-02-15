<template>
  <div
    id="calculate"
    class="form-calculate container-wrapper bg-g"
  >
    <div class="container fd-c ai-c py-100 py-50-mb">
      <h2 class="header-text z-1 mb-50 mb-35-mb">
        Страхование несчастных случаев
      </h2>
      <div class="w-100 px-100 px-0-mb">
        <AppForm
          ref="observerCalc"
          class="w-100 bg-w bs-1 br-30 p-55 bg-g-mb bs-n-mb p-0-mb"
          :gy="50"
          :gy-mb="25"
          @submit="validateForm"
        >
          <div class="form-calculate__days">
            <div class="fw-6 fs-25 lh-140 mb-70 ws-nw">
              Срок страхования
            </div>
            <AppFormField
              class="px-20"
              vid="term"
            >
              <AppInput
                v-if="$mq === 'mb'"
                id="termInput"
                v-model="data.count_days"
                type="tel"
                class="form-calculate__term form-calculate__term--input"
                component="InputNumber"
                :min="1"
                :max="365"
              />
              <AppSlider
                id="term"
                v-model="data.count_days"
                :min="1"
                :max="365"
                @change="changeSlider"
              />
            </AppFormField>
          </div>
          <div class="form-calculate__slider">
            <div class="fw-6 fs-25 lh-140 mb-70 ws-nw mt-50">
              Сумма страхования
            </div>
            <div class="fw-4 fs-10 lh-140 mb-70 ws-nw mt-50">
              Смерть Застрахованного в результате несчастного<br> случая, происшедшего в период страхования
            </div>
            <AppFormField
              class="px-20"
              vid="sum"
            >
              <AppSlider
                id="sum"
                v-model="data.sum"
                :min="50000"
                :max="1000000"
                :step="50000"
                @change="changeSliderSum"
              />
            </AppFormField>
          </div>

          <div class="form-calculate__slider">
            <div class="fw-4 fs-10 lh-140 mb-70 ws-nw mt-50">
              Установление Застрахованному I или II или<br>
              III группы инвалидности в результате несчастного<br>
              случая, происшедшего в период страхования
            </div>
            <AppFormField
              class="px-20"
              vid="sum_disability"
            >
              <AppSlider
                id="sum_disability"
                v-model="data.sum_disability"
                :disabled="!selectedRisks.accident_disability"
                :min="50000"
                :max="500000"
                :step="50000"
                @change="changeSliderSumDisabilty"
              />
            </AppFormField>
          </div>

          <div class="form-calculate__slider">
            <div class="fw-4 fs-10 lh-140 mb-70 ws-nw mt-50">
              Временная нетрудоспособность Застрахованного<br>
              в результате несчастного случая, произошедшего<br>
              в период страхования
            </div>
            <AppFormField
              class="px-20"
              vid="sum_accident"
            >
              <AppSlider
                id="sum_accident"
                v-model="data.sum_accident"
                :disabled="!selectedRisks.timedisability_accident"
                :min="50000"
                :max="300000"
                :step="50000"
                @change="changeSliderSumAccident"
              />
            </AppFormField>
          </div>

          <div class="lh-140 fs-16-mb">
            <div class="fw-6 fs-25 lh-140 my-20 ws-nw mt-50-mb">
              Риски
            </div>
            <AppFormField
              vid="risks"
            >
              <AppCheckbox
                id="risks-1"
                v-model="data.risks"
                class-checkbox="mt-5"
                value-label="accident_death"
                :disabled="true"
                @input="checkCalculateProp('accident_death', data.risks.includes('accident_death'))"
              >
                <label
                  for="risks-1"
                  class="ml-10"
                >
                  Смерть Застрахованного в результате несчастного случая,<br>
                  происшедшего в период страхования
                </label>
              </AppCheckbox>
              <AppCheckbox
                id="risks-2"
                v-model="data.risks"
                class="mt-10"
                class-checkbox="mt-5"
                value-label="accident_disability"
                @input="checkCalculateProp('accident_disability', data.risks.includes('accident_disability'))"
              >
                <label
                  for="risks-2"
                  class="ml-10"
                >
                  Установление Застрахованному I или II или III группы инвалидности<br>
                  в результате несчастного случая, происшедшего в период страхования
                </label>
              </AppCheckbox>
              <AppCheckbox
                id="risks-3"
                v-model="data.risks"
                class="mt-10"
                class-checkbox="mt-5"
                value-label="timedisability_accident"
                @input="checkCalculateProp('timedisability_accident', data.risks.includes('timedisability_accident'))"
              >
                <label
                  for="risks-3"
                  class="ml-10"
                >
                  Временная нетрудоспособность Застрахованного в результате<br>
                  несчастного случая, произошедшего в период страхования
                </label>
              </AppCheckbox>
            </AppFormField>
          </div>
          <div>
            <div class="fw-6 fs-25 lh-140 mb-10 ws-nw">
              Категория спорта
              <span class="fw-4 fs-12 o-50 ml-10 lh-110 d-b-mb ml-0-mb">
                (до 5 видов спорта)
              </span>
            </div>
            <div class="d-f ai-c fd-c-mb w-100-mb ai-fs-mb">
              <AppFormField
                class="w-100-mb"
                vid="sport"
              >
                <AppMultiSelect
                  id="sport"
                  ref="select"
                  v-model="data.type_of_sport"
                  class="form-calculate__dropdown w-100-mb"
                  :class="{ 'error': isErrorSelect }"
                  filter
                  filter-placeholder="Найти вид спорта"
                  empty-filter-message="Вид спорта не найден"
                  placeholder="Выбрать категорию"
                  :options="optionsSport"
                  :selection-limit="5"
                  @input="onSelectInput"
                />
                <div
                  v-if="isErrorSelect"
                  class="app-form-field__error c-e pos-a fs-14 ws-nw l-0"
                >
                  Необходимо выбрать хотя бы 1 вид спорта
                </div>
              </AppFormField>
              <AppFormField
                vid="proffesional"
                class="ml-20 ml-0-mb mt-30-mb"
              >
                <AppInputSwitch
                  id="proffesional"
                  v-model="data.is_professional"
                  name="proffesional"
                  label="Я профессионал"
                  @input="checkCalculateProp('is_professional', $event)"
                />
              </AppFormField>
            </div>
          </div>
          <div>
            <div class="fw-6 fs-25 lh-140 mb-10 ws-nw">
              Промокод
            </div>
            <div class="d-f ai-c fd-c-mb w-100-mb ai-fs-mb">
              <AppFormField
                vid="promo"
              >
                <AppInput
                  id="promo"
                  v-model="data.promo"
                  component="InputText"
                  placeholder="########"
                  :class="{ 'error': promo_required_error }"
                  @input="() => {promo_required_error = false; checkCalculateProp('promo', data.promo)}"
                />
                <div v-if="promo_required_error" class="app-form-field__error c-e pos-a fs-14 ws-nw l-0" style="margin-bottom: 4px">
                  Необходимо ввести промокод!
                </div>
                <AppInputGroup />
              </AppFormField>
              <AppButton
                class="ml-20 ml-0-mb mt-15-mb ord-3-mb w-100-mb"
                label="Рассчитать"
                type="submit"
                :loading="loading"
                :disabled="loading"
              />
              <AppFormField
                vid="sport"
                class="ml-20 ml-0-mb mt-15-mb"
              >
                <AppInputSwitch
                  id="partner"
                  v-model="data.partner"
                  name="partner"
                  label="Я партнёр"
                  @input="checkCalculateProp('partner', $event)"
                />
              </AppFormField>
            </div>
            <div class="mt-25 mt-35-mb">
              <AppFormField
                vid="rulespol"
                rules="istrue"
                error-position="left"
                class=""
              >
                <AppCheckbox
                  id="rulespol"
                  v-model="data.rulespol"
                  class="ai-c"
                  binary
                  @input="checkCalculateProp('rulespol', $event)"
                >
                  <label
                    for="rulespol"
                    class="ml-10 fs-16-mb"
                  >
                    Я согласен с правилами пользования
                  </label>
                </AppCheckbox>
              </AppFormField>
            </div>
          </div>
          <div v-if="priceString" class="d-f fd-c fs-25 lh-140 fs-22-mb lh-120-mb">
            <div>Предварительная стоимость Вашего полиса:</div>
            <div class="fs-40 c-p fw-7 mt-15-mb">
              {{ priceString }}
            </div>
            <div class="fs-16 o-50 mt-10 fs-12-mb lh-120-mb">
              Предварительный расчет.<br class="d-n d-b-mb">
              Не является публичной офертой
            </div>
          </div>
        </AppForm>
      </div>
    </div>
    <ClientOnly>
      <Teleport
        to=".form-calculate__days .app-slider"
      >
        <div
          ref="term"
          class="form-calculate__term bg-w b-1 br-5 py-10 d-f jc-c d-n-mb"
        >
          {{ termString }}
        </div>
      </Teleport>
      <Teleport
        to=".form-calculate__slider #sum"
      >
        <div
          ref="sum"
          class="form-calculate__sum bg-w b-1 br-5 py-10 d-f jc-c"
        >
          {{ termStringSum }}
        </div>
      </Teleport>

      <Teleport
        to=".form-calculate__slider #sum_disability"
      >
        <div
          ref="sum_disability"
          class="form-calculate__sum bg-w b-1 br-5 py-10 d-f jc-c"
        >
          {{ termStringSumDisability }}
        </div>
      </Teleport>

      <Teleport
        to=".form-calculate__slider #sum_accident"
      >
        <div
          ref="sum_accident"
          class="form-calculate__sum bg-w b-1 br-5 py-10 d-f jc-c"
        >
          {{ termStringSumAccident }}
        </div>
      </Teleport>

      <Teleport
        to="#term"
      >
        <div class="form-calculate__term--mobile d-n d-b-mb">
          {{ termDay }}
        </div>
        <div class="form-calculate__circle pos-a l-0 br-c" />
        <div class="form-calculate__circle pos-a r-0 br-c" />
      </Teleport>
      <Teleport
        to="#sum"
      >
        <div class="form-calculate__circle pos-a l-0 br-c" />
        <div class="form-calculate__circle pos-a r-0 br-c" />
      </Teleport>
    </ClientOnly>
  </div>
</template>

<script>
import sportList from './sport-list';
export default {
  name: 'TheFormCalculate',
  props: {
    price: {
      type: Number,
      default: null,
    },

    loading: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    data: {
      count_days: 1,
      sum: 200000,
      sum_disability: 200000,
      sum_accident: 200000,
      type_of_sport: [],
      is_professional: false,
      risks: [
        'accident_death',
        'accident_disability',
        'timedisability_accident',
      ],

      is_sporttime: false,

      // promo: 'VECTORSPORT',
      promo: null,
      partner: false,
      rulespol: false,
    },

    promo_required_error: false,

    optionsSport: sportList,
    sliderHandleEl: null,
    sliderHandleElSum: null,
    sliderHandleElSumDisability: null,
    sliderHandleElSumAccident: null,
    isErrorSelect: false,

    tooltipOptions: {
      content: `
        «НС во время занятий спортом» означает, что страхование распространяется только на время,
        когда спортсмен тренируется или участвует в соревнованиях. Если признак не установлен,
        то страхование распространяется как на время тренировок/соревнований, так и другое время,
        когда спортсмен не занимается спортом
      `,
      placement: 'right',
    },
    tooltipOptionsMobile: {
      content: `
        «НС во время занятий спортом» означает, что страхование распространяется только на время,
        когда спортсмен тренируется или участвует в соревнованиях. Если признак не установлен,
        то страхование распространяется как на время тренировок/соревнований, так и другое время,
        когда спортсмен не занимается спортом
      `,
      trigger: 'click',
      // placement: 'right',
    },
  }),
  computed: {
    termDay() {
      const div = (val, by) => {
        return (val - val % by) / by;
      }
      const mod = (val, by) => {
        return val % by;
      }

      if (
        div(mod(this.data.count_days, 100), 10) === 1 ||
        mod(this.data.count_days, 10) > 4 ||
        mod(this.data.count_days, 10) === 0
      ) {
        return 'дней';
      }
      if (mod(this.data.count_days, 10) > 1) {
        return 'дня';
      }
      return 'день';
    },
    termString() {
      return `${this.data.count_days} ${this.termDay}`;
    },
    termStringSum() {
      return `${this.data.sum} ₽`;
    },
    termStringSumDisability() {
      return `${this.data.sum_disability} ₽`;
    },
    termStringSumAccident() {
      return `${this.data.sum_accident} ₽`;
    },
    priceString() {
      return this.price ? `${this.price.toLocaleString()} ₽` : null;
    },
    selectedRisks() {
      return {
        accident_death: this.data.risks.includes('accident_death'),
        accident_disability: this.data.risks.includes('accident_disability'),
        timedisability_accident: this.data.risks.includes('timedisability_accident'),
      }
    },
  },
  watch: {
    'data.type_of_sport'(value) {
      if (value.length === 5) {
        this.$refs.select.$el.classList.add('full');
        return;
      }
      this.$refs.select.$el.classList.remove('full');
    },
  },
  mounted() {
    this.sliderHandleEl = document.querySelector('.form-calculate__days .p-slider-handle');
    this.sliderHandleElSum = document.querySelector('.form-calculate__slider #sum .p-slider-handle');
    this.sliderHandleElSumDisability = document.querySelector('.form-calculate__slider #sum_disability .p-slider-handle');
    this.sliderHandleElSumAccident = document.querySelector('.form-calculate__slider #sum_accident .p-slider-handle');
  },
  created() {
    this.getPromoFromUrl();
  },
  methods: {
    changeSliderSum(value) {
      let left = Number(this.sliderHandleElSum.style.left.replace('%', ''));
      if (left < 4.7) {
        left = 4.7;
      }
      if (left > 95.3) {
        left = 95.3;
      }
      this.$refs.sum.style.left = left + '%';
      this.checkCalculateProp('sum', value);
    },
    changeSliderSumDisabilty(value) {
      let left = Number(this.sliderHandleElSumDisability.style.left.replace('%', ''));
      if (left < 4.7) {
        left = 4.7;
      }
      if (left > 95.3) {
        left = 95.3;
      }
      this.$refs.sum_disability.style.left = left + '%';
      this.checkCalculateProp('sum_disability', value);
    },
    changeSliderSumAccident(value) {
      let left = Number(this.sliderHandleElSumAccident.style.left.replace('%', ''));
      if (left < 4.7) {
        left = 4.7;
      }
      if (left > 95.3) {
        left = 95.3;
      }
      this.$refs.sum_accident.style.left = left + '%';
      this.checkCalculateProp('sum_accident', value);
    },
    onSelectInput(value) {
      this.validateSelect();
      this.checkCalculateProp('type_of_sport', value.join(';'));
    },
    changeSlider(value) {
      let left = Number(this.sliderHandleEl.style.left.replace('%', ''));
      if (left < 4.7) {
        left = 4.7;
      }
      if (left > 95.3) {
        left = 95.3;
      }
      this.$refs.term.style.left = left + '%';

      this.checkCalculateProp('count_days', value);
    },
    async validateForm() {
      const isValidForm = await this.$refs.observerCalc.validate();

      this.validateSelect();

      if (!this.data.promo) {
        this.promo_required_error = true;
      }

      if (!isValidForm || this.isErrorSelect || !this.data.promo) {
        return;
      }

      this.$emit('fetch-calculate', this.prepareFormData());
    },
    prepareFormData() {
      const formData = {
        accident_death: this.selectedRisks.accident_death ? this.data.sum : 0,
        accident_disability: this.selectedRisks.accident_disability ? this.data.sum_disability : 0,
        time_disability_accident: this.selectedRisks.timedisability_accident ? this.data.sum_accident : 0,
        timedisability_accident: this.selectedRisks.timedisability_accident ? this.data.sum_accident : 0,
        is_sporttime: this.data.is_sporttime,
        is_professional: this.data.is_professional,
        count_days: this.data.count_days,
        type_of_sport: this.data.type_of_sport.length > 0 ? this.data.type_of_sport.join(';') : undefined,
        promo: this.data.promo,
        partner: this.data.partner,
      };

      // Удаляем пустые ключи
      Object.keys(formData).forEach(key => (formData[key] === undefined || formData[key] === null) && delete formData[key]);

      return formData;
    },
    validateSelect() {
      this.isErrorSelect = this.data.type_of_sport.length === 0;
    },

    getPromoFromUrl() {
      const promocode = this.$route.query.promocode;
      if (promocode) {
        this.data.promo = promocode;
      }
    },

    checkCalculateProp(prop, value) {
      this.$emit('check-calculate-prop', prop, value);
    },
  },
}
</script>

<style lang="scss">
  .form-calculate__slider {
    .app-slider {
      color: #444444;
      &::before {
        position: absolute;
        left: 0;
        top: 2rem;
        transform: translateX(-29%);
      }
      &::after {
        position: absolute;
        right: 0;
        top: 2rem;
        transform: translateX(20%);
      }
    }

    .app-slider[disabled="disabled"] {
      opacity: 0.5
    }

    #sum {
      color: #444444;
      &::before {
        content: '50000 ₽';
      }
      &::after {
        content: '1000000 ₽';
      }
    }

    #sum_disability {
      color: #444444;
      &::before {
        content: '50000 ₽';
      }
      &::after {
        content: '500000 ₽';
      }
    }

    #sum_accident {
      color: #444444;
      &::before {
        content: '50000 ₽';
      }
      &::after {
        content: '300000 ₽';
      }
    }
  }

.form-calculate {
  /* .form-calculate__term */
  .app-input.form-calculate__term--input {
    left: 0;
    top: -6rem;
    transform: none;
    padding: .5rem 1rem;
    border-radius: .5rem;
    width: 6rem;
    .p-inputnumber-input {
      font-size: 2rem;
      text-align: center;
    }
  }

  &__term, &__sum {
    position: absolute;
    white-space: nowrap;
    border-color: #D2D2D2;
    width: 15rem;
    left: 4.7%;
    top: -6rem;
    transform: translateX(-50%);
    &--mobile {
      position: absolute;
      top: -5rem;
      left: 5rem;
    }
  }
  &__sum {
    left: 60%;
  }
  /* .form-calculate__circle */
  &__circle {
    width: 1.8rem;
    height: 1.8rem;
    background: $primary;
    top: -.6rem;
    transform: translateX(-40%);
    & + & {
      background: $gray-dd;
      transform: translateX(40%);
    }
  }
  /* .form-calculate__dropdown */
  &__dropdown {
    width: 40rem;
    &.full {
      .p-multiselect-items {
        cursor: default;
      }
      .p-multiselect-item:not(.p-highlight) {
        opacity: .5;
      }
    }
    @media (max-width: 600px) {
      width: 100%;
    }
  }
  &__days {
    .app-slider {
    color: #444444;
    &::before {
      position: absolute;
      left: 0;
      top: 2rem;
      transform: translateX(-29%);
      content: '1 день';
    }
    &::after {
      position: absolute;
      right: 0;
      top: 2rem;
      transform: translateX(20%);
      content: '365 дней';
    }
  }
  }
  .p-slider-handle {
    z-index: 1;
    &::before {
      position: absolute;
    }
  }
  .app-multi-select.error {
    border: 1px solid $error;
    box-shadow: 0 0 .3rem rgba(255, 0, 0, 0.4) ;
  }
}
</style>
