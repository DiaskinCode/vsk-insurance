<template>
  <div class="form-order container fd-c ai-c py-100 py-50-mb">
    <h2 class="header-text mb-50 mb-25-mb">
      Оформить заявку
    </h2>
    <AppForm
      class="w-100 px-100 px-0-mb"
      ref="observer"
      :gy="45"
      :gy-mb="25"
      @submit="validateForm"
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
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="birth_policyholder"
              rules="required"
              label="Дата рождения страхователя"
            >
              <AppInput
                id="birth_policyholder"
                v-model="data.birth_policyholder"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="fio_insured_person"
              rules="required"
              label="ФИО застрахованного лица"
            >
              <AppInput
                id="fio_insured_person"
                v-model="data.fio_insured_person"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="birth_insured_person"
              rules="required"
              label="Дата рождения застрахованного лица"
            >
              <AppInput
                id="birth_insured_person"
                v-model="data.birth_insured_person"
                component="InputText"
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
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="email_policyholder"
              rules="required"
              label="Email страхователя"
            >
              <AppInput
                id="email_policyholder"
                v-model="data.email_policyholder"
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
          :loading="loading"
          :disabled="loading"
        />
        <AppButton
          class="ml-25 ml-5-mb fg-1-mb"
          secondary
          label="Предпросмотр"
          :loading="loading"
          :disabled="loading"
        />
      </div>
    </AppForm>
  </div>
</template>

<script>
export default {
  name: 'TheFormOrder',
  props: {},
  data: () => ({
    loading: false,
    data: {
      fio_policyholder: '',
      birth_policyholder: '',

      fio_insured_person: '',
      birth_insured_person: '',

      phone_policyholder: '',
      email_policyholder: '',
    },
  }),
  computed: {},
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
</style>
