<template>
  <div class="include container fd-c ai-c py-100">
    <h2 class="fw-7 fs-40 lh-110 c-t1b">Что включает полис</h2>
    <div class="fw-5 fs-30 lh-140 mt-10">Риски:</div>
    <div class="row gx-25 fs-25 lh-140 mt-50">
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
