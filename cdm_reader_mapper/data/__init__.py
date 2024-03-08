"""Common Data Model (CDM) reader and mapper test data."""

from __future__ import annotations

import os


class test_data:
    """CDM test data."""

    def __init__(self):
        self._data_path = os.path.dirname(os.path.abspath(__file__))

        self.test_063_714 = self._get_data_dict(
            "063-714_2010-07-01_subset.imma", "imma1_d714", "714", "imma1", "icoads_r3000",
        )
        self.test_069_701 = self._get_data_dict(
            "069-701_1845-04-01_subset.imma", "imma1_d701", "701", "imma1", "icoads_r3000",
        )
        self.test_084_706 = self._get_data_dict(
            "084-706_1919-03-01_subset.imma", "imma1_d705-707", "706", "imma1", "icoads_r3000",
        )
        self.test_085_705 = self._get_data_dict(
            "085-705_1938-04-01_subset.imma", "imma1_d705-707", "705", "imma1", "icoads_r3000",
        )
        self.test_096_702 = self._get_data_dict(
            "096-702_1873-01-01_subset.imma", "imma1_d702", "702", "imma1", "icoads_r3000",
        )
        self.test_098_707 = self._get_data_dict(
            "098-707_1916-04-01_subset.imma", "imma1_d705-707", "707", "imma1", "icoads_r3000",
        )
        self.test_103_794 = self._get_data_dict(
            "103-794_2021-11-01_subset.imma", "imma1_nodt", "794", "imma1", "icoads_r3000_NRT",
        )
        self.test_125_704 = self._get_data_dict(
            "125-704_1878-10-01_subset.imma", "imma1_d704", "704", "imma1", "icoads_r3000",
        )
        self.test_125_721 = self._get_data_dict(
            "125-721_1862-06-01_subset.imma", "imma1_d721", "721", "imma1", "icoads_r3000",
        )
        self.test_133_730 = self._get_data_dict(
            "133-730_1776-10-01_subset.imma", "imma1_d730", "730", "imma1", "icoads_r3000",
        )
        self.test_143_781 = self._get_data_dict(
            "143-781_1987-09-01_subset.imma", "imma1_d781", "781", "imma1", "icoads_r3000",
        )
        self.test_144_703 = self._get_data_dict(
            "144-703_1979-09-01_subset.imma", "imma1", "703", "imma1", "icoads_r3000",
        )
        self.test_091_201 = self._get_data_dict(
            "091-201_1913-11-01_subset.imma", "imma1", "201", "imma1", "icoads_r3000",
        )
        self.test_077_892 = self._get_data_dict(
            "077-892_1996-02-01_subset.imma", "imma1", "892", "imma1", "icoads_r3000",
        )
        self.test_147_700 = self._get_data_dict(
            "147-700_2002-08-01_subset.imma", "imma1", "700", "imma1", "icoads_r3000",
        )
        self.test_103_792 = self._get_data_dict(
            "103-792_2017-02-01_subset.imma", "imma1_nodt", "792", "imma1", "icoads_r3000_NRT",
        )
        self.test_114_992 = self._get_data_dict(
            "114-992_2016-01-01_subset.imma", "imma1_nodt", "792", "imma1", "icoads_r3000_NRT",
        )
        self.test_gcc_mix = self._get_data_dict("mix_out_20030201.immt", "gcc_immt", "???", "immt", "gdac_r0000",)

    def __getitem__(self, attr):
        """Make class subscriptable."""
        try:
            return getattr(self, attr)
        except AttributeError as err:
            raise KeyError(attr) from err

    def _get_data_dict(self, data_file, schema, deck, dm, ds):
        return {
            "source": os.path.join(self._data_path, data_file),
            "data_model": schema,
            "dm": dm,
            "ds": ds,
            "deck": deck,
        }


test_data = test_data()
