<template>
  <div class="form-order container fd-c ai-c py-100 py-50-mb">
    <h2 class="header-text mb-50 mb-25-mb">
      Оформить полис
    </h2>
    <AppForm
      class="w-100 px-100 px-0-mb"
      ref="observer"
      :gy="45"
      :gy-mb="25"
      @submit="validateForm('post-buy')"
    >
      <div>
        <div class="fw-6 fs-25 lh-140 mb-15 ws-nw">
          Персональные данные
        </div>
        <div>
          <AppFormRow
            :gx="25"
            :gy="20"
          >
            <AppFormField
              class="col-6 col-12-mb"
              vid="fio_policyholder"
              rules="required"
              label="ФИО страхователя"
            >
              <AppInput
                id="fio_policyholder"
                v-model="data.fio_policyholder"
                placeholder="Фамилия Имя Отчество"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="birth_policyholder"
              :rules="rulesPolicyholder"
              label="Дата рождения страхователя"
            >
              <AppInput
                id="birth_policyholder"
                v-model="data.birth_policyholder"
                component="InputText"
                v-mask="'##.##.####'"
                type="tel"
                placeholder="ДД.ММ.ГГГГ"
              />
            </AppFormField>

            <AppFormField
              class="col-12"
              vid="same-checkbox"
            >
              <AppCheckbox
                id="same-checkbox"
                v-model="isSame"
                class="ai-c"
                binary
              >
                <label
                  for="same-checkbox"
                  class="ml-10 fs-16 fs-15-mb"
                >
                  Застрахованное лицо является страхователем
                </label>
              </AppCheckbox>
            </AppFormField>

            <AppFormField
              v-if="!isSame"
              class="col-6 col-12-mb"
              vid="fio_insured_person"
              rules="required"
              label="ФИО застрахованного лица"
            >
              <AppInput
                id="fio_insured_person"
                v-model="data.fio_insured_person"
                placeholder="Фамилия Имя Отчество"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              v-if="!isSame"
              class="col-6 col-12-mb"
              vid="birth_insured_person"
              rules="required|date|insured-person-min|insured-person-max"
              label="Дата рождения застрахованного лица"
            >
              <AppInput
                id="birth_insured_person"
                v-model="data.birth_insured_person"
                component="InputText"
                v-mask="'##.##.####'"
                type="tel"
                placeholder="ДД.ММ.ГГГГ"
              />
            </AppFormField>
          </AppFormRow>
        </div>
      </div>
      <div>
        <div class="fw-6 fs-25 lh-140 mb-15 ws-nw">
          Контактные данные
        </div>
        <div>
          <AppFormRow
            :gx="25"
            :gy="20"
          >
            <AppFormField
              class="col-6 col-12-mb"
              vid="phone_policyholder"
              rules="required"
              label="Телефон страхователя"
            >
              <AppInput
                id="phone_policyholder"
                v-model="data.phone_policyholder"
                component="InputText"
                v-mask="'+7 (###) ###-##-##'"
                type="tel"
                placeholder="+7 (999) 999-99-99"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="email_policyholder"
              rules="required|email"
              label="Email страхователя"
            >
              <AppInput
                id="email_policyholder"
                v-model="data.email_policyholder"
                type="email"
                placeholder="yourmail@gmail.com"
                component="InputText"
              />
            </AppFormField>
          </AppFormRow>
        </div>
      </div>
      <div class="d-f">
        <AppButton
          class="fg-1-mb"
          label="Оформить"
          type="submit"
          :loading="loadingBuy"
          :disabled="loadingGetdraft || loadingBuy || !isEnabled || !isSameData"
        />
        <AppButton
          class="ml-25 ml-5-mb fg-1-mb"
          secondary
          label="Предпросмотр"
          :loading="loadingGetdraft"
          :disabled="loadingBuy || loadingGetdraft || !isEnabled || !isSameData"
          @click="validateForm('post-getdraft')"
        />
      </div>
    </AppForm>
    <div
      v-if="!isEnabled"
      class="fs-16 o-50 as-fs pl-100 mt-20 fs-12-mb pl-0-mb"
    >
      Сначала необходимо<br class="d-n d-b-mb">
      рассчитать стоимость полиса.
    </div>
    <div
      v-if="!isSameData"
      class="fs-16 o-50 as-fs pl-100 mt-20 fs-12-mb pl-0-mb"
    >
      Даные в рассчетах изменены.<br class="d-n d-b-mb">
      Необходимо рассчитать стоимость полиса.
    </div>
  </div>
</template>

<script>
import datetoolsMixin from '~/mixins/datetools';
export default {
  name: 'TheFormOrder',
  mixins: [
    datetoolsMixin,
  ],
  props: {
    isEnabled: {
      type: Boolean,
      default: false,
    },
    isSameData: {
      type: Boolean,
      default: false,
    },

    loadingGetdraft: {
      type: Boolean,
      default: false,
    },
    loadingBuy: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    data: {
      fio_policyholder: '',
      birth_policyholder: '',

      fio_insured_person: '',
      birth_insured_person: '',

      phone_policyholder: '',
      email_policyholder: '',
    },

    isSame: false,

    // data: {
    //   fio_policyholder: '123',
    //   birth_policyholder: '12.12.2000',

    //   fio_insured_person: '123 123 123',
    //   birth_insured_person: '12.12.2000',

    //   phone_policyholder: '',
    //   email_policyholder: 'alex@alex.ru',
    // },
  }),
  computed: {
    rulesPolicyholder() {
      return {
        required: true,
        date: true,
        'policyholder-min': true,
        'insured-person-max': this.isSame,
      }
    }
  },
  methods: {
    async validateForm(method) {
      const isValidForm = await this.$refs.observer.validate();
      if (!isValidForm) {
        return;
      }
      this.$emit(method, this.prepareFormData());
    },
    prepareFormData() {
      const formData = { ...this.data };
      formData.birth_policyholder = this.ruDateToISO(formData.birth_policyholder);
      formData.birth_insured_person = this.ruDateToISO(formData.birth_insured_person);
      formData.phone_policyholder = '+' + formData.phone_policyholder.replace(/\D/g, '');

      if (this.isSame) {
        formData.fio_insured_person = formData.fio_policyholder;
        formData.birth_insured_person = formData.birth_policyholder;
      }

      return formData;
    },
  },
}
</script>

<style lang="scss">
</style>
