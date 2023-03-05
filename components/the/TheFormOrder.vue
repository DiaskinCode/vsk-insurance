<template>
  <div class="form-order container fd-c ai-c py-100">
    <h2 class="header-text mb-50">
      Оформить заявку
    </h2>
    <AppForm
      class="w-100"
      ref="observer"
      :gy="45"
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
              vid="insurerFio"
              rules="required"
              label="ФИО страхователя"
            >
              <AppInput
                id="insurerFio"
                v-model="data.insurerFio"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="insurerBirthday"
              rules="required"
              label="Дата рождения страхователя"
            >
              <AppInput
                id="insurerBirthday"
                v-model="data.insurerBirthday"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="personFio"
              rules="required"
              label="ФИО застрахованного лица"
            >
              <AppInput
                id="personFioe"
                v-model="data.personFio"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="personBirthday"
              rules="required"
              label="Дата рождения застрахованного лица"
            >
              <AppInput
                id="personBirthday"
                v-model="data.personBirthday"
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
              vid="phone"
              rules="required"
              label="ФИО страхователя"
            >
              <AppInput
                id="phone"
                v-model="data.phone"
                component="InputText"
              />
            </AppFormField>
            <AppFormField
              class="col-6 col-12-mb"
              vid="email"
              rules="required"
              label="Дата рождения страхователя"
            >
              <AppInput
                id="email"
                v-model="data.email"
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
      insurerFio: '',
      insurerBirthday: '',
      personFio: '',
      personBirthday: '',
      phone: '',
      email: '',
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
