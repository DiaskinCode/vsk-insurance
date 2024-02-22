<template>
  <Accordion
    class="app-accordion"
    expand-icon="pi-chevron-left"
    collapse-icon="pi-chevron-left expand"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template
      v-for="(_, slot) of $scopedSlots"
      #[slot]="scope"
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
.app-accordion {
  .p-accordion-header-text {
    font-weight: 600;
    font-size: 3.2rem;
    line-height: 123%;
    color: $text-15;
    @media (max-width: 600px) {
      font-size: 1.6rem;
      line-height: 110%;
    }
  }
  .p-accordion-toggle-icon {
    display: none;
    color: $primary;
    transition: transform .2s ease;
    margin-left: .5rem;
    font-size: 1.5rem;
    &.expand {
      transform: rotate(-90deg);
    }
    @media (max-width: 600px) {
      display: block;
    }
  }
  .p-accordion-tab {
    background: $white;
    box-shadow: 0px .4rem 5rem rgba(0, 0, 0, 0.05);
    border-radius: 3rem;
    padding-bottom: 5rem;
    @media (max-width: 600px) {
      border-radius: 1rem;
      padding-bottom: 0rem;
    }
  }
  .p-accordion-header {
    padding: 5rem 4rem 0 5rem;
    @media (max-width: 600px) {
      border-radius: 1rem;
      padding: 1.3rem 2rem;
      box-shadow: 0px .4rem 1.5rem rgba(0, 0, 0, 0.04);
    }
  }
  .p-toggleable-content {
    padding: 0 4rem 0 5rem;
    @media (max-width: 600px) {
      padding: 0 2rem 0rem;
    }
  }
  .p-accordion-header-link {
    @media (max-width: 600px) {
      flex-direction: row-reverse;

    }
  }
  .p-accordion-content {
    font-size: 2rem;
    line-height: 140%;
    color: $text-15;
    margin-top: 2rem;
    @media (max-width: 600px) {
      font-size: 1.6rem;
      margin-top: 1.5rem;
      margin-bottom: 1.5rem;
    }
  }
}
</style>
