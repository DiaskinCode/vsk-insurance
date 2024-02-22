<template>
  <div
    id="include"
    class="include container fd-c ai-c py-100 ai-fs-mb py-50-mb"
  >
    <h2 class="header-text">
      Что включает полис
    </h2>
    <div class="fw-5 fs-30 lh-140 mt-10 fs-25-mb">
      Риски:
    </div>
    <div class="row gx-25 gy-10 fs-25 lh-140 mt-40 fs-16-mb lh-120-mb mt-15-mb">
      <IncludeListItem class="col">
        <h3>
          <span class="fw-7">Смерть</span>
          в результате несчастного случая
        </h3>
      </IncludeListItem>
      <IncludeListItem class="col">
        <h3>
          <span class="fw-7">Инвалидность</span><br>
          в результате
          несчастного случая
        </h3>
      </IncludeListItem>
      <IncludeListItem class="col">
        <h3>
          <span class="fw-7">Травмы</span>
          в результате
          несчастного случая
        </h3>
      </IncludeListItem>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheInclude',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
</style>
