<template>
  <Timeline
    class="app-timeline"
    :value="value"
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
  </Timeline>
</template>

<script>
export default {
  name: 'AppTimeline',
  props: {
    value: {
      type: Array,
      required: true,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.app-timeline {
  &.p-timeline.p-timeline-horizontal .p-timeline-event-connector {
      height: 0.3rem;
  }
  &.p-timeline.p-timeline-vertical .p-timeline-event-connector {
    width: 2px;
  }
  &.p-timeline .p-timeline-event-connector {
      background-color: #F5F6F9;
  }

  &.p-timeline.p-timeline-vertical .p-timeline-event-content {
    padding: 0 1rem;
  }
  &.p-timeline.p-timeline-horizontal .p-timeline-event-content {
    padding: 1rem 0;
  }
  .p-timeline-event-opposite {
    max-height: 0;
    max-width: 0;
  }
}
</style>
