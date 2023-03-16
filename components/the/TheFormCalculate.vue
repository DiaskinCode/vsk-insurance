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
          <div>
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
              >
                <label
                  for="risks-3"
                  class="ml-10"
                >
                  Временная нетрудоспособность Застрахованного в результате<br>
                  несчастного случая, произошедшего в период страхования
                </label>
              </AppCheckbox>
              <div class="d-f ai-c pt-20 ">
                <AppCheckbox
                  id="risks-4"
                  binary
                  v-model="data.is_sporttime"
                  class="ai-c"
                >
                  <label
                    for="risks-4"
                    class="ml-10"
                  >
                    НС во время занятий спортом
                  </label>
                </AppCheckbox>
                <div
                  class="ml-15"
                  v-tooltip="tooltipOptions"
                >
                  <i class="pi pi-question-circle fs-16 o-50" />
                </div>
              </div>
            </AppFormField>
          </div>
          <div>
            <div class="fw-6 fs-25 lh-140 mb-10 ws-nw">
              Категория спорта
            </div>
            <div class="d-f ai-c fd-c-mb w-100-mb ai-fs-mb">
              <AppFormField
                class="w-100-mb"
                vid="sport"
              >
                <AppMultiSelect
                  id="sport"
                  v-model="data.type_of_sport"
                  class="form-calculate__dropdown w-100-mb"
                  :class="{ 'error': isErrorSelect }"
                  filter
                  filterPlaceholder="Найти вид спорта"
                  emptyFilterMessage="Вид спорта не найден"
                  placeholder="Выбрать категорию"
                  :options="optionsSport"
                  @input="onSelectInput"
                />
                <div
                  v-if="isErrorSelect"
                  class="app-form-field__error c-e pos-a fs-14"
                >
                  Необходимо выбрать хотя бы 1 вид спорта
                </div>
              </AppFormField>
              <AppFormField
                vid="proffesional"
                class="ml-20 ml-0-mb mt-15-mb"
              >
                <AppInputSwitch
                  id="proffesional"
                  v-model="data.is_professional"
                  name="proffesional"
                  label="Я профессионал"
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
                vid="sport"
              >
                <AppInput
                  id="promocode"
                  v-model="data.promo"
                  component="InputText"
                />
                </AppInputGroup>
              </AppFormField>
              <AppButton
                class="ml-20 ml-0-mb mt-15-mb ord-3-mb w-100-mb"
                label="Рассчитать"
                type="submit"
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
                />
              </AppFormField>
            </div>
            <div class="mt-25 mt-35-mb">
              <AppFormField
                vid="rulespol"
                rules="istrue"
                errorPosition="left"
                class=""
              >
                <AppCheckbox
                  id="rulespol"
                  v-model="data.rulespol"
                  class="ai-c"
                  binary
                >
                  <label
                    for="rulespol"
                    class="ml-10 fs-16-mb"
                  >
                    Я согласен с <AppLinkInner>правилами пользования</AppLinkInner>
                  </label>
                </AppCheckbox>
              </AppFormField>
            </div>
          </div>
          <div class="d-f fd-c fs-25 lh-140 fs-22-mb lh-120-mb" v-if="priceString">
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
        to=".form-calculate .app-slider"
      >
        <div
          ref="term"
          class="form-calculate__term bg-w b-1 br-5 py-10 d-f jc-c d-n-mb"
        >
          {{ termString }}
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
  },
  data: () => ({
    loading: false,
    data: {
      count_days: 1,
      type_of_sport: [],
      is_professional: false,
      risks: ['accident_death'],
      is_sporttime: false,

      promo: '',
      partner: false,
      rulespol: false,
    },
    optionsSport: sportList,
    sliderHandleEl: null,
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
  mounted() {
    this.sliderHandleEl = document.querySelector('.p-slider-handle');
  },
  methods: {
    onSelectInput(val) {
      this.validateSelect();
    },
    changeSlider() {
      let left = Number(this.sliderHandleEl.style.left.replace('%', ''));
      if (left < 4.7) {
        left = 4.7;
      }
      if (left > 95.3) {
        left = 95.3;
      }
      this.$refs.term.style.left = left + '%';
    },
    async validateForm() {
      const isValidForm = await this.$refs.observerCalc.validate();
      this.validateSelect();
      if (!isValidForm || this.isErrorSelect) {
        return;
      }
      const formData = { ...this.selectedRisks };
      formData.is_professional = this.data.is_professional;
      formData.count_days = this.data.count_days;
      formData.type_of_sport = this.data.type_of_sport;

      this.$emit('fetch-calculate', this.prepareFormData());
    },
    prepareFormData() {
      const formData = { ...this.selectedRisks };
      formData.is_sporttime = this.data.is_sporttime;
      formData.is_professional = this.data.is_professional;
      formData.count_days = this.data.count_days;
      formData.type_of_sport = this.data.type_of_sport.join(';');
      formData.promo = this.data.promo;
      return formData;
    },
    validateSelect() {
      this.isErrorSelect = this.data.type_of_sport.length === 0;
    },
  },
}
</script>

<style lang="scss">
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

  &__term {
    position: absolute;
    white-space: nowrap;
    border-color: #D2D2D2;
    width: 12rem;
    left: 4.7%;
    top: -6rem;
    transform: translateX(-50%);
    &--mobile {
      position: absolute;
      top: -5rem;
      left: 5rem;
    }
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
    @media (max-width: 600px) {
      width: 100%;
    }
  }
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
  .p-slider-handle {
    z-index: 1;
    &::before {
      position: absolute;
    }
  }
  .app-multi-select.error {
    border: 1px solid $error;
    box-shadow: 0px 0rem .3rem rgba(255, 0, 0, 0.4) ;
  }

}
</style>
