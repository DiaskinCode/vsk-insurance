<template>
  <Accordion
    class="app-accordion"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template
      v-for="(_, slot) of $scopedSlots"
      v-slot:[slot]="scope"
    >
      <slot
        :name="slot"
        v-bind="scope"
      />
    </template>
  </Accordion>
</template>

<script>
export default {
  name: 'AppAccordion',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.p-accordion-header-text {
  font-weight: 600;
  font-size: 3.2rem;
  line-height: 123%;
  color: $text-15;
}
.p-accordion-toggle-icon {
  display: none;
}
.p-accordion-tab {
  background: $white;
  box-shadow: 0px .4rem 5rem rgba(0, 0, 0, 0.05);
  border-radius: 3rem;
  padding: 5rem;
  padding-right: 4rem;
}
.p-accordion-content {
  font-size: 2rem;
  line-height: 140%;
  color: $text-15;
  margin-top: 2rem;
}
</style>
