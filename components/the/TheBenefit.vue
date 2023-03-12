<template>
  <div
    id="benefit"
    class="benefit container-wrapper bg-g"
  >
    <div class="container fd-c ai-c py-100 ai-fs-mb py-50-mb">
      <h2 class="header-text">Преимущества</h2>
      <div class="mt-50">
        <div class="
          row gy-30 fs-20 lh-140 px-100
          gy-50-mb fs-16-mb lh-130-mb px-0-mb
        ">
          <BenefitListItem
            src="/benefit/1.svg"
          >
            <h3>
              В полис включены актуальные риски несчастного случая, которые
              защищают вас и вашего ребенка на время занятий следующими
              видами спорта на любительском уровне
            </h3>
          </BenefitListItem>
          <BenefitListItem
            src="/benefit/2.svg"
          >
            <h3>
              Полис подходит для предоставления в спортивные секции или
              для участия в соревнованиях.
            </h3>
          </BenefitListItem>
          <BenefitListItem
            src="/benefit/3.svg"
          >
            <h3>
              В случае страхового события у вас и вашего ребенка будет
              «финансовая подушка безопасности» в виде денежной выплаты,
              которую можно потратить на лечение, лекарства и реабилитацию
              в хороших клиниках
            </h3>
          </BenefitListItem>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheBebefit',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
</style>
